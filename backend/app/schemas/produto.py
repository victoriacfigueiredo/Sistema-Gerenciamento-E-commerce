from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.avaliacoes_pedidos import AvaliacaoPedidoResponse

class ProdutoBase(BaseModel):
    nome_produto: str
    categoria_produto: str
    peso_produto_gramas: Optional[float] = None
    comprimento_centimetros: Optional[float] = None
    altura_centimetros: Optional[float] = None
    largura_centimetros: Optional[float] = None


class ProdutoCreate(ProdutoBase):
    id_produto: str

class ProdutoUpdate(BaseModel):
    nome_produto: Optional[str] = None
    categoria_produto: Optional[str] = None
    peso_produto_gramas: Optional[float] = None
    comprimento_centimetros: Optional[float] = None
    altura_centimetros: Optional[float] = None
    largura_centimetros: Optional[float] = None

class ProdutoResponse(ProdutoBase):
    id_produto: str
    model_config = ConfigDict(from_attributes=True)

class ProdutoMetricasResponse(BaseModel):
    total_vendas: int
    faturamento_total: float
    total_avaliacoes: int
    media_avaliacoes: Optional[float] = None

class ProdutoDetalheResponse(ProdutoResponse):
    metricas: ProdutoMetricasResponse
    avaliacoes: list[AvaliacaoPedidoResponse]

