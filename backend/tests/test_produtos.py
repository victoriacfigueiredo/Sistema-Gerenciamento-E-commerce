def criar_produto_exemplo(client, id_produto="prod001", nome="Mouse Gamer", categoria="Informatica"):
    payload = {
        "id_produto": id_produto,
        "nome_produto": nome,
        "categoria_produto": categoria,
        "peso_produto_gramas": 250,
        "comprimento_centimetros": 12,
        "altura_centimetros": 4,
        "largura_centimetros": 6,
    }
    return client.post("/produtos/", json=payload)


def criar_dados_relacionados_para_detalhes(client):
    from app.models.consumidor import Consumidor
    from app.models.vendedor import Vendedor
    from app.models.pedido import Pedido
    from app.models.item_pedido import ItemPedido
    from app.models.avaliacao_pedido import AvaliacaoPedido
    from tests.conftest import TestingSessionLocal

    db = TestingSessionLocal()
    try:
        consumidor = Consumidor(
            id_consumidor="cons001",
            prefixo_cep="50000",
            nome_consumidor="Victor",
            cidade="Recife",
            estado="PE",
        )
        vendedor = Vendedor(
            id_vendedor="vend001",
            nome_vendedor="Loja XPTO",
            prefixo_cep="50000",
            cidade="Recife",
            estado="PE",
        )
        pedido = Pedido(
            id_pedido="ped001",
            id_consumidor="cons001",
            status="entregue",
        )
        item = ItemPedido(
            id_pedido="ped001",
            id_item=1,
            id_produto="prod001",
            id_vendedor="vend001",
            preco_BRL=100.0,
            preco_frete=20.0,
        )
        avaliacao = AvaliacaoPedido(
            id_avaliacao="ava001",
            id_pedido="ped001",
            avaliacao=5,
            titulo_comentario="Excelente",
            comentario="Produto muito bom",
        )

        db.add(consumidor)
        db.add(vendedor)
        db.add(pedido)
        db.add(item)
        db.add(avaliacao)
        db.commit()
    finally:
        db.close()


def test_criar_produto(client):
    response = criar_produto_exemplo(client)

    assert response.status_code == 201
    data = response.json()

    assert data["id_produto"] == "prod001"
    assert data["nome_produto"] == "Mouse Gamer"
    assert data["categoria_produto"] == "Informatica"


def test_nao_deve_criar_produto_duplicado(client):
    criar_produto_exemplo(client)
    response = criar_produto_exemplo(client)

    assert response.status_code == 409
    assert response.json()["detail"] == "Produto já existe"


def test_listar_produtos(client):
    criar_produto_exemplo(client, id_produto="prod001", nome="Mouse Gamer")
    criar_produto_exemplo(client, id_produto="prod002", nome="Teclado Mecânico")

    response = client.get("/produtos/")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 2
    assert data[0]["id_produto"] == "prod001"
    assert data[1]["id_produto"] == "prod002"


def test_obter_produto_por_id(client):
    criar_produto_exemplo(client)

    response = client.get("/produtos/prod001")

    assert response.status_code == 200
    data = response.json()

    assert data["id_produto"] == "prod001"
    assert data["nome_produto"] == "Mouse Gamer"


def test_retornar_404_ao_obter_produto_inexistente(client):
    response = client.get("/produtos/inexistente")

    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"


def test_buscar_produtos(client):
    criar_produto_exemplo(client, id_produto="prod001", nome="Mouse Gamer", categoria="Informatica")
    criar_produto_exemplo(client, id_produto="prod002", nome="Teclado Mecânico", categoria="Informatica")
    criar_produto_exemplo(client, id_produto="prod003", nome="Cadeira Escritório", categoria="Moveis")

    response = client.get("/produtos/busca?q=Mouse")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["id_produto"] == "prod001"


def test_atualizar_produto(client):
    criar_produto_exemplo(client)

    payload = {
        "nome_produto": "Mouse Gamer Pro",
        "categoria_produto": "Periféricos",
    }

    response = client.put("/produtos/prod001", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["nome_produto"] == "Mouse Gamer Pro"
    assert data["categoria_produto"] == "Periféricos"


def test_deletar_produto(client):
    criar_produto_exemplo(client)

    response = client.delete("/produtos/prod001")
    assert response.status_code == 204

    response_get = client.get("/produtos/prod001")
    assert response_get.status_code == 404


def test_detalhar_produto_com_metricas_e_avaliacoes(client):
    criar_produto_exemplo(client)
    criar_dados_relacionados_para_detalhes(client)

    response = client.get("/produtos/prod001/detalhes")

    assert response.status_code == 200
    data = response.json()

    assert data["id_produto"] == "prod001"
    assert data["peso_produto_gramas"] == 250
    assert data["metricas"]["total_vendas"] == 1
    assert data["metricas"]["faturamento_total"] == 100.0
    assert data["metricas"]["total_avaliacoes"] == 1
    assert data["metricas"]["media_avaliacoes"] == 5.0
    assert len(data["avaliacoes"]) == 1
    assert data["avaliacoes"][0]["id_avaliacao"] == "ava001"


def test_retornar_404_ao_detalhar_produto_inexistente(client):
    response = client.get("/produtos/produto-inexistente/detalhes")

    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"