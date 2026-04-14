# Sistema de Gerenciamento E-commerce

Um sistema completo de e-commerce com arquitetura de microserviços, dividido em frontend e backend, com funcionalidades de gestão de produtos, pedidos, consumidores e vendedores.

---

## 📋 Visão Geral

O projeto é composto por duas partes principais:

- **Backend**: API REST construída com FastAPI e SQLite
- **Frontend**: Interface web construída com React, TypeScript e Vite

---

## 🏗️ Arquitetura

```
Sistema de Gerenciamento E-commerce
│
├── Backend (FastAPI)
│   ├── Models (SQLAlchemy)
│   ├── Routers (APIs REST)
│   ├── Schemas (Validação Pydantic)
│   ├── Database (SQLite)
│   └── Migrations (Alembic)
│
└── Frontend (React)
    ├── Components (UI)
    ├── Services (API Client)
    ├── Types (TypeScript)
    └── Vite (Build Tool)
```

---

## 🚀 Quick Start

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- Git

### 1. Clone o repositório

```bash
git clone <repo-url>
cd Sistema-Gerenciamento-E-commerce
```

### 2. Configure o Backend

```bash
cd backend

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrations
alembic upgrade head

# Inicie o servidor
python -m app.main
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)  
Documentação: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Configure o Frontend

```bash
cd frontend

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

A aplicação estará disponível em: [http://localhost:5173](http://localhost:5173)

---

## 📁 Estrutura do Projeto

```
Sistema-Gerenciamento-E-commerce/
│
├── backend/
│   ├── app/
│   │   ├── main.py                  # Ponto de entrada
│   │   ├── database.py              # Configuração do banco
│   │   ├── config.py                # Variáveis de ambiente
│   │   ├── models/                  # Models SQLAlchemy
│   │   │   ├── consumidor.py
│   │   │   ├── produto.py
│   │   │   ├── vendedor.py
│   │   │   ├── pedido.py
│   │   │   ├── item_pedido.py
│   │   │   └── avaliacao_pedido.py
│   │   ├── schemas/                 # Schemas Pydantic
│   │   │   ├── produto.py
│   │   │   └── avaliacoes_pedidos.py
│   │   └── routers/                 # Rotas da API
│   │       └── produtos.py
│   ├── alembic/                     # Migrations
│   ├── scripts/
│   │   └── seed.py                  # População de dados
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_produtos.py
│   ├── data/                        # Dados de exemplo (CSV)
│   ├── requirements.txt
│   ├── alembic.ini
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── main.tsx                 # Ponto de entrada
│   │   ├── App.tsx                  # Componente principal
│   │   ├── components/              # Componentes reutilizáveis
│   │   │   ├── ProductCard.tsx
│   │   │   ├── ProductForm.tsx
│   │   │   ├── ProductSearch.tsx
│   │   │   └── StatsPanel.tsx
│   │   ├── services/                # Serviços (API Client)
│   │   │   └── api.ts
│   │   ├── types/                   # Tipos TypeScript
│   │   │   └── product.ts
│   │   ├── data/                    # Dados e constantes
│   │   └── assets/
│   ├── index.html
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── eslint.config.js
│   ├── package.json
│   └── README.md
│
└── README.md (este arquivo)
```

---

## 🔑 Principais Funcionalidades

### Backend

- ✅ CRUD completo de Produtos
- ✅ Gerenciamento de Consumidores
- ✅ Gerenciamento de Vendedores
- ✅ Gestão de Pedidos
- ✅ Itens de Pedido
- ✅ Avaliações de Pedidos
- ✅ Busca e filtros
- ✅ Métricas e relatórios
- ✅ Validação de dados com Pydantic
- ✅ Testes unitários com pytest

### Frontend

- ✅ Listagem de produtos
- ✅ Formulário de criação/edição de produtos
- ✅ Busca de produtos
- ✅ Painel de estatísticas
- ✅ Interface responsiva
- ✅ Integração com API REST
- ✅ Type-safe com TypeScript

---

## 🧪 Testes

### Backend

```bash
cd backend

# Executar todos os testes
pytest tests/

# Executar com cobertura
pytest tests/ --cov=app

# Executar teste específico
pytest tests/test_produtos.py::test_criar_produto
```

Testes disponíveis:
- Criação de produtos
- Validação de duplicação
- Listagem e busca
- Obtenção por ID
- Atualização
- Deleção
- Detalhes com métricas e avaliações

---

## 🗄️ Banco de Dados

### Setup

```bash
cd backend

# Criar tabelas
alembic upgrade head

# Ver estado atual
alembic current

# Criar nova migration
alembic revision -m "descricao"

# Reverter última migration
alembic downgrade -1
```

### Entidades

- **Consumidor**: Compradores do e-commerce
- **Vendedor**: Fornecedores de produtos
- **Produto**: Itens à venda
- **Pedido**: Compras realizadas
- **ItemPedido**: Produtos em um pedido
- **AvaliacaoPedido**: Reviews dos pedidos

---

## 📚 Documentação

- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger)

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM para Python
- **Pydantic** - Validação de dados
- **Alembic** - Migrations de banco de dados
- **pytest** - Framework de testes
- **SQLite** - Banco de dados

### Frontend
- **React** - Biblioteca UI
- **TypeScript** - Tipagem estática
- **Vite** - Build tool
- **ESLint** - Linting

---

## 📋 Scripts Úteis

### Backend

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python -m app.main

# Rodar testes
pytest tests/

# Popular banco com dados
python scripts/seed.py
```

### Frontend

```bash
# Instalar dependências
npm install

# Rodar em desenvolvimento
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview

# Lint
npm run lint
```

