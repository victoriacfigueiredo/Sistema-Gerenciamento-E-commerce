from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from app.database import get_db
from app.models.avaliacao_pedido import AvaliacaoPedido
from app.models.item_pedido import ItemPedido
from app.models.pedido import Pedido
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoDetalheResponse, ProdutoMetricasResponse, ProdutoResponse, ProdutoUpdate

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(payload: ProdutoCreate, db: Session = Depends(get_db)):
    produto_existente = db.get(Produto, payload.id_produto)

    if produto_existente:
        raise HTTPException(status_code=409, detail="Produto já existe")

    novo_produto = Produto(**payload.model_dump())

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

@router.get("/busca", response_model=list[ProdutoResponse])
def buscar_produtos(
    q: str = Query(..., min_length=1),
    skip: int = 0,
    limit: int = Query(default=20, le=100),
    db: Session = Depends(get_db),
):
    termo = f"%{q}%"

    produtos = (
        db.query(Produto)
        .filter(
            or_(
                Produto.id_produto.ilike(termo),
                Produto.nome_produto.ilike(termo),
                Produto.categoria_produto.ilike(termo),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )

    return produtos

@router.get("/{id_produto}", response_model=ProdutoResponse)
def obter_produto(id_produto: str, db: Session = Depends(get_db)):
    produto = db.get(Produto, id_produto)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto

@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(
    skip: int = 0,
    limit: int = Query(default=20, le=100),
    db: Session = Depends(get_db)
):
    produtos = db.query(Produto).offset(skip).limit(limit).all()
    return produtos

@router.get("/{id_produto}/detalhes", response_model=ProdutoDetalheResponse)
def detalhar_produto(id_produto: str, db: Session = Depends(get_db)):
    produto = db.get(Produto, id_produto)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    total_vendas = (
        db.query(func.count())
        .select_from(ItemPedido)
        .filter(ItemPedido.id_produto == id_produto)
        .scalar()
    ) or 0

    faturamento_total = (
        db.query(func.coalesce(func.sum(ItemPedido.preco_BRL), 0.0))
        .filter(ItemPedido.id_produto == id_produto)
        .scalar()
    ) or 0.0

    avaliacoes = (
        db.query(AvaliacaoPedido)
        .join(Pedido, Pedido.id_pedido == AvaliacaoPedido.id_pedido)
        .join(ItemPedido, ItemPedido.id_pedido == Pedido.id_pedido)
        .filter(ItemPedido.id_produto == id_produto)
        .distinct(AvaliacaoPedido.id_avaliacao)
        .all()
    )

    total_avaliacoes = len(avaliacoes)
    media_avaliacoes = None

    if total_avaliacoes > 0:
        media_avaliacoes = round(sum(av.avaliacao for av in avaliacoes) / total_avaliacoes,2)

    return ProdutoDetalheResponse(
        id_produto=produto.id_produto,
        nome_produto=produto.nome_produto,
        categoria_produto=produto.categoria_produto,
        peso_produto_gramas=produto.peso_produto_gramas,
        comprimento_centimetros=produto.comprimento_centimetros,
        altura_centimetros=produto.altura_centimetros,
        largura_centimetros=produto.largura_centimetros,
        metricas=ProdutoMetricasResponse(
            total_vendas=total_vendas,
            faturamento_total=round(float(faturamento_total),2),
            total_avaliacoes=total_avaliacoes,
            media_avaliacoes=media_avaliacoes,
        ),
        avaliacoes=avaliacoes,
    )

@router.put("/{id_produto}", response_model=ProdutoResponse)
def atualizar_produto(
    id_produto: str,
    payload: ProdutoUpdate,
    db: Session = Depends(get_db),
):
    produto = db.get(Produto, id_produto)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    for campo, valor in payload.model_dump(exclude_unset=True).items():
        setattr(produto, campo, valor)

    db.commit()
    db.refresh(produto)

    return produto


@router.delete("/{id_produto}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(id_produto: str, db: Session = Depends(get_db)):
    produto = db.get(Produto, id_produto)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()