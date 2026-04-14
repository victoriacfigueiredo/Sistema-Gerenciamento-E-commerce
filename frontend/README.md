# Frontend — Sistema de Compras Online

Interface web construída com **React**, **TypeScript** e **Vite**, consumindo a API REST do backend.

---

## Requisitos

- Node.js 18+
- npm ou yarn

---

## Instalação

**1. Instale as dependências**

```bash
npm install
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (opcional, o padrão aponta para `http://localhost:8000`):

```bash
VITE_API_BASE_URL=http://localhost:8000
```

---

## Rodando a Aplicação

### Modo de desenvolvimento

```bash
npm run dev
```

A aplicação estará disponível em: [http://localhost:5173](http://localhost:5173)

## Estrutura do Projeto

```
frontend/
├── src/
│   ├── main.tsx             # Ponto de entrada da aplicação
│   ├── App.tsx              # Componente principal
│   ├── App.css              # Estilos globais
│   ├── index.css            # Estilos base
│   ├── assets/              # Arquivos estáticos (imagens, ícones, etc)
│   ├── components/          # Componentes reutilizáveis
│   │   ├── ProductCard.tsx      # Exibe um produto em card
│   │   ├── ProductForm.tsx      # Formulário para criar/editar produtos
│   │   ├── ProductSearch.tsx    # Barra de busca de produtos
│   │   └── StatsPanel.tsx       # Painel de estatísticas
│   ├── services/            # Serviços de integração com API
│   │   └── api.ts               # Cliente HTTP para comunicação com backend
│   ├── types/               # Tipos e interfaces TypeScript
│   │   └── product.ts           # Tipos relacionados a produtos
│   └── data/                # Dados e constantes
│       └── imagensPorCategoria.ts   # Mapeamento de imagens por categoria
├── public/
├── index.html
├── eslint.config.js         # Configuração do ESLint
├── vite.config.ts           # Configuração do Vite
├── tsconfig.json            # Configuração principal TypeScript
├── tsconfig.app.json        # Configuração TypeScript para aplicação
├── tsconfig.node.json       # Configuração TypeScript para ferramentas
├── package.json
└── README.md
```

