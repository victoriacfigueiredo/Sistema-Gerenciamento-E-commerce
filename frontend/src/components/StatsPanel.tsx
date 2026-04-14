import type { ProductDetails } from "../types/product";
import { getImagemProduto } from "../data/imagensPorCategoria";

interface StatsPanelProps {
  product: ProductDetails | null;
}

export function StatsPanel({ product }: StatsPanelProps) {
  if (!product) {
    return (
      <section className="details-panel empty-state">
        <h2>Selecione um produto</h2>
        <p>Escolha um item do catálogo para ver métricas e avaliações.</p>
      </section>
    );
  }

  return (
    <section className="details-panel">
      <div className="details-hero">
        <img
          src={getImagemProduto(product.categoria_produto)}
          alt={product.nome_produto}
          className="details-image"
        />

        <div className="details-summary">
          <span className="badge">{product.categoria_produto}</span>

          <h2>{product.nome_produto}</h2>

          <p>ID: {product.id_produto}</p>

          <div className="metrics-grid">
            <div className="metric-card">
              <span>Total de vendas</span>
              <strong>{product.metricas.total_vendas}</strong>
            </div>

            <div className="metric-card">
              <span>Faturamento</span>
              <strong>
                R$ {product.metricas.faturamento_total.toFixed(2)}
              </strong>
            </div>

            <div className="metric-card">
              <span>Total de avaliações</span>
              <strong>{product.metricas.total_avaliacoes}</strong>
            </div>

            <div className="metric-card">
              <span>Média das avaliações</span>
              <strong>
                {product.metricas.media_avaliacoes !== null
                  ? product.metricas.media_avaliacoes.toFixed(2)
                  : "Sem avaliações"}
              </strong>
            </div>
          </div>
        </div>
      </div>

      <div className="details-sections">
        <div className="section-card">
          <h3>Medidas do produto 📦</h3>

          <div className="dimensions-grid">
            <div>
              <span>Peso</span>
              <strong>{product.peso_produto_gramas ?? "-"} g</strong>
            </div>

            <div>
              <span>Comprimento</span>
              <strong>{product.comprimento_centimetros ?? "-"} cm</strong>
            </div>

            <div>
              <span>Altura</span>
              <strong>{product.altura_centimetros ?? "-"} cm</strong>
            </div>

            <div>
              <span>Largura</span>
              <strong>{product.largura_centimetros ?? "-"} cm</strong>
            </div>
          </div>
        </div>

        <div className="section-card">
          <h3>Avaliações dos consumidores ⭐</h3>

          {product.avaliacoes.length === 0 ? (
            <p>Nenhuma avaliação encontrada.</p>
          ) : (
            <div className="reviews-list">
              {product.avaliacoes.map((review) => (
                <article
                  key={review.id_avaliacao}
                  className="review-card"
                >
                  <div className="review-header">
                    <strong>
                      {review.titulo_comentario || "Sem título"}
                    </strong>

                    <span>Nota: {review.avaliacao}/5</span>
                  </div>

                  <p>{review.comentario || "Sem comentário."}</p>

                  <small>Pedido: {review.id_pedido}</small>
                </article>
              ))}
            </div>
          )}
        </div>
      </div>
    </section>
  );
}