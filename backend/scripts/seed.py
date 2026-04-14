from pathlib import Path
from datetime import datetime, date
import csv

from app.database import SessionLocal
from app.models.consumidor import Consumidor
from app.models.vendedor import Vendedor
from app.models.produto import Produto
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.models.avaliacao_pedido import AvaliacaoPedido

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def parse_float(value):
    if value in (None, "", "null"):
        return None
    return float(value)


def parse_int(value):
    if value in (None, "", "null"):
        return None
    return int(value)


def parse_datetime(value):
    if value in (None, "", "null"):
        return None
    return datetime.fromisoformat(value)


def parse_date(value):
    if value in (None, "", "null"):
        return None
    return date.fromisoformat(value)


def importar_consumidores(db):
    arquivo = DATA_DIR / "dim_consumidores.csv"
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = Consumidor(
                id_consumidor=row["id_consumidor"],
                prefixo_cep=row["prefixo_cep"],
                nome_consumidor=row["nome_consumidor"],
                cidade=row["cidade"],
                estado=row["estado"],
            )
            db.merge(obj)
    db.commit()
    print("Consumidores importados")


def importar_vendedores(db):
    arquivo = DATA_DIR / "dim_vendedores.csv"
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = Vendedor(
                id_vendedor=row["id_vendedor"],
                nome_vendedor=row["nome_vendedor"],
                prefixo_cep=row["prefixo_cep"],
                cidade=row["cidade"],
                estado=row["estado"],
            )
            db.merge(obj)
    db.commit()
    print("Vendedores importados")


def importar_produtos(db):
    arquivo = DATA_DIR / "dim_produtos.csv"
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = Produto(
                id_produto=row["id_produto"],
                nome_produto=row["nome_produto"],
                categoria_produto=row["categoria_produto"],
                peso_produto_gramas=parse_float(row["peso_produto_gramas"]),
                comprimento_centimetros=parse_float(row["comprimento_centimetros"]),
                altura_centimetros=parse_float(row["altura_centimetros"]),
                largura_centimetros=parse_float(row["largura_centimetros"]),
            )
            db.merge(obj)
    db.commit()
    print("Produtos importados")


def importar_pedidos(db):
    arquivo = DATA_DIR / "fat_pedidos.csv"
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = Pedido(
                id_pedido=row["id_pedido"],
                id_consumidor=row["id_consumidor"],
                status=row["status"],
                pedido_compra_timestamp=parse_datetime(row["pedido_compra_timestamp"]),
                pedido_entregue_timestamp=parse_datetime(row["pedido_entregue_timestamp"]),
                data_estimada_entrega=parse_date(row["data_estimada_entrega"]),
                tempo_entrega_dias=parse_float(row["tempo_entrega_dias"]),
                tempo_entrega_estimado_dias=parse_float(row["tempo_entrega_estimado_dias"]),
                diferenca_entrega_dias=parse_float(row["diferenca_entrega_dias"]),
                entrega_no_prazo=row["entrega_no_prazo"] or None,
            )
            db.merge(obj)
    db.commit()
    print("Pedidos importados")


def importar_itens_pedidos(db):
    arquivo = DATA_DIR / "fat_itens_pedidos.csv"
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = ItemPedido(
                id_pedido=row["id_pedido"],
                id_item=parse_int(row["id_item"]),
                id_produto=row["id_produto"],
                id_vendedor=row["id_vendedor"],
                preco_BRL=parse_float(row["preco_BRL"]),
                preco_frete=parse_float(row["preco_frete"]),
            )
            db.merge(obj)
    db.commit()
    print("Itens de pedidos importados")


def importar_avaliacoes_pedidos(db):
    arquivo = DATA_DIR / "fat_avaliacoes_pedidos.csv"

    ids_vistos = set()
    duplicados = 0

    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            id_avaliacao = row["id_avaliacao"]

            if id_avaliacao in ids_vistos:
                duplicados += 1
                continue

            ids_vistos.add(id_avaliacao)

            obj = AvaliacaoPedido(
                id_avaliacao=id_avaliacao,
                id_pedido=row["id_pedido"],
                avaliacao=parse_int(row["avaliacao"]),
                titulo_comentario=row["titulo_comentario"] or None,
                comentario=row["comentario"] or None,
                data_comentario=parse_datetime(row["data_comentario"]),
                data_resposta=parse_datetime(row["data_resposta"]),
            )

            db.add(obj)

    db.commit()

    print("Avaliações importadas")
    print(f"Duplicados ignorados: {duplicados}")


def main():
    db = SessionLocal()
    try:
        importar_consumidores(db)
        importar_vendedores(db)
        importar_produtos(db)
        importar_pedidos(db)
        importar_itens_pedidos(db)
        importar_avaliacoes_pedidos(db)
        print("Seed finalizado com sucesso")
    finally:
        db.close()


if __name__ == "__main__":
    main()