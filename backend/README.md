# Backend — Sistema de Compras Online

API REST construída com **FastAPI** e **SQLite**, utilizando SQLAlchemy como ORM e Alembic para migrations.

---

## Requisitos

- Python 3.11+

---

## Instalação

**1. Crie e ative um ambiente virtual**

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**

Copie o arquivo de exemplo e ajuste se necessário:

```bash
cp .env.example .env
```

---

## Banco de dados

### Criar as tabelas

```bash
alembic upgrade head
```

Este comando lê os arquivos dentro de `alembic/versions/` e cria todas as tabelas no banco.

### Ver o estado atual

```bash
alembic current
```

### Criar uma nova migration (após alterar um model)

```bash
alembic revision -m "descricao da mudanca"
```

Depois edite o arquivo gerado em `alembic/versions/` adicionando as instruções em `upgrade()` e `downgrade()`.

### Desfazer a última migration

```bash
alembic downgrade -1
```

---

## Rodando a API

```bash
python -m app.main
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

Documentação: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Testes

Os testes são executados com **pytest** e utilizam um banco de dados SQLite em memória para isolamento.

### Executar todos os testes

```bash
pytest tests/
```

### Executar um teste específico

```bash
pytest tests/test_produtos.py::test_criar_produto
```

### Executar com cobertura de código

```bash
pytest tests/ --cov=app
```

### Testes disponíveis

- **test_produtos.py** - Testes da API de produtos
  - `test_criar_produto` - Criar um novo produto
  - `test_nao_deve_criar_produto_duplicado` - Validar duplicação
  - `test_listar_produtos` - Listar todos os produtos
  - `test_obter_produto_por_id` - Obter produto por ID
  - `test_retornar_404_ao_obter_produto_inexistente` - Tratamento de não encontrado
  - `test_buscar_produtos` - Buscar produtos por query
  - `test_atualizar_produto` - Atualizar dados do produto
  - `test_deletar_produto` - Deletar um produto
  - `test_detalhar_produto_com_metricas_e_avaliacoes` - Detalhes com métricas e avaliações
  - `test_retornar_404_ao_detalhar_produto_inexistente` - Detalhes de produto inexistente

---

## Estrutura do projeto

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── database.py          # Configuração do banco de dados
│   ├── config.py            # Variáveis de ambiente
│   ├── models/              # Models do SQLAlchemy 
│   │   ├── __init__.py
│   │   ├── consumidor.py
│   │   ├── produto.py
│   │   ├── vendedor.py
│   │   ├── pedido.py
│   │   ├── item_pedido.py
│   │   └── avaliacao_pedido.py
│   ├── schemas/             # Schemas do Pydantic
│   │   ├── __init__.py
│   │   ├── produto.py
│   │   └── avaliacoes_pedidos.py
│   └── routers/             # Rotas da API
│       ├── __init__.py
│       └── produtos.py
├── alembic/
│   ├── env.py               # Configuração do Alembic
│   ├── script.py.mako
│   └── versions/            # Arquivos de migration
│       └── 001_initial_schema.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Configuração dos testes
│   └── test_produtos.py     # Testes da API de produtos
├── scripts/
│   └── seed.py              # Script para popular o banco
├── data/
│   ├── dim_consumidores.csv
│   ├── dim_produtos.csv
│   ├── dim_vendedores.csv
│   ├── fat_avaliacoes_pedidos.csv
│   ├── fat_itens_pedidos.csv
│   └── fat_pedidos.csv
├── alembic.ini              # Configuração principal do Alembic
├── requirements.txt
├── README.md
└── .env.example
```
