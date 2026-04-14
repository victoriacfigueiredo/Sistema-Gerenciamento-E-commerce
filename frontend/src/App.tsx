import { useEffect, useMemo, useState } from "react";
import {
  createProduct,
  deleteProduct,
  getProductDetails,
  getProducts,
  searchProducts,
  updateProduct,
} from "./services/api";
import { ProductCard } from "./components/ProductCard";
import { ProductForm } from "./components/ProductForm";
import { ProductSearch } from "./components/ProductSearch";
import { StatsPanel } from "./components/StatsPanel";
import type { Product, ProductDetails, ProductFormData } from "./types/product";

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [selectedDetails, setSelectedDetails] = useState<ProductDetails | null>(null);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [page, setPage] = useState(1);

  const limit = 12;

  const selectedProduct = useMemo(
    () => products.find((product) => product.id_produto === selectedId) ?? null,
    [products, selectedId]
  );

  async function loadProducts(currentPage = 1) {
    try {
      setLoading(true);
      setError(null);

      const skip = (currentPage - 1) * limit;
      const data = await getProducts(skip, limit);

      setProducts(data);

      if (data.length > 0) {
        setSelectedId(data[0].id_produto);
      } else {
        setSelectedId(null);
        setSelectedDetails(null);
      }
    } catch {
      setError("Não foi possível carregar os produtos.");
    } finally {
      setLoading(false);
    }
  }

  async function loadDetails(id: string) {
    try {
      setError(null);
      const data = await getProductDetails(id);
      setSelectedDetails(data);
    } catch {
      setSelectedDetails(null);
      setError("Não foi possível carregar os detalhes do produto.");
    }
  }

  useEffect(() => {
    if (!search.trim()) {
      loadProducts(page);
    }
  }, [page]);

  useEffect(() => {
    if (selectedId) {
      loadDetails(selectedId);
    }
  }, [selectedId]);

  async function handleSearch() {
    try {
      setLoading(true);
      setError(null);

      if (!search.trim()) {
        setPage(1);
        await loadProducts(1);
        return;
      }

      const data = await searchProducts(search.trim());
      setProducts(data);

      if (data.length > 0) {
        setSelectedId(data[0].id_produto);
      } else {
        setSelectedId(null);
        setSelectedDetails(null);
      }
    } catch {
      setError("Não foi possível buscar produtos.");
    } finally {
      setLoading(false);
    }
  }

  async function handleClear() {
    setSearch("");
    setPage(1);
    await loadProducts(1);
  }

  async function handleCreate(payload: ProductFormData) {
    try {
      setError(null);
      await createProduct(payload);
      setSearch("");
      setPage(1);
      await loadProducts(1);
      setSelectedId(payload.id_produto);
    } catch {
      setError("Não foi possível criar o produto.");
    }
  }

  async function handleUpdate(
    id: string,
    payload: Omit<ProductFormData, "id_produto">
  ) {
    try {
      setError(null);
      await updateProduct(id, payload);

      if (search.trim()) {
        await handleSearch();
      } else {
        await loadProducts(page);
      }

      await loadDetails(id);
    } catch {
      setError("Não foi possível atualizar o produto.");
    }
  }

  async function handleDelete(id: string) {
    const confirmed = window.confirm("Deseja remover este produto?");
    if (!confirmed) return;

    try {
      setError(null);
      await deleteProduct(id);

      if (search.trim()) {
        await handleSearch();
      } else {
        await loadProducts(page);
      }

      setSelectedDetails(null);
      setSelectedId(null);
    } catch {
      setError("Não foi possível remover o produto.");
    }
  }

  return (
    <div className="page-shell">
      <header className="hero">
        <div>
          <span className="hero-kicker">Painel gerencial</span>
          <h1> Rocket Lab E-commerce </h1>
          <p>
            Visualize catálogo, métricas de vendas, avaliações e operações de
            cadastro em um único painel administrativo.
          </p>
        </div>
      </header>

      <ProductSearch
        value={search}
        onChange={setSearch}
        onSearch={handleSearch}
        onClear={handleClear}
      />

      {error && <div className="alert-error">{error}</div>}

      <main className="main-grid">
        <section className="catalog-panel">
          <div className="catalog-header">
            <h2>Produtos</h2>
          </div>

          <div className="products-grid">
            {products.map((product) => (
              <ProductCard
                key={product.id_produto}
                product={product}
                selected={product.id_produto === selectedId}
                onSelect={setSelectedId}
              />
            ))}
          </div>

          {!search.trim() && (
            <div className="pagination-wrapper">
              <div className="pagination">
                <button
                  className="btn btn-page"
                  onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
                  disabled={page === 1 || loading}
                >
                  ← Anterior
                </button>

                <span className="pagination-info">Página {page}</span>

                <button
                  className="btn btn-page"
                  onClick={() => {
                    if (products.length === limit) {
                      setPage((prev) => prev + 1);
                    }
                  }}
                  disabled={loading || products.length < limit}
                >
                  Próxima →
                </button>
              </div>
            </div>
          )}
        </section>

        <aside className="side-panel">
          <StatsPanel product={selectedDetails} />
          <ProductForm
            selectedProduct={selectedProduct}
            onCreate={handleCreate}
            onUpdate={handleUpdate}
            onDelete={handleDelete}
          />
        </aside>
      </main>
    </div>
  );
}

export default App;