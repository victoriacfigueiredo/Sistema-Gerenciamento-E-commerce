import type { Product } from "../types/product";
import { getImagemProduto } from "../data/imagensPorCategoria";

interface ProductCardProps {
  product: Product;
  onSelect: (id: string) => void;
  selected: boolean;
}

export function ProductCard({
  product,
  onSelect,
  selected,
}: ProductCardProps) {
  return (
    <button
      className={`product-card ${selected ? "product-card-selected" : ""}`}
      onClick={() => onSelect(product.id_produto)}
    >
      <img
        src={getImagemProduto(product.categoria_produto)}
        alt={product.nome_produto}
        className="product-image"
      />

      <div className="product-card-body">
        <span className="badge">{product.categoria_produto}</span>

        <h3>{product.nome_produto}</h3>

        <p className="product-id">ID: {product.id_produto}</p>

        <div className="product-dimensions">
          <span>{product.peso_produto_gramas ?? "-"} g</span>
          <span>{product.comprimento_centimetros ?? "-"} cm</span>
          <span>{product.altura_centimetros ?? "-"} cm</span>
          <span>{product.largura_centimetros ?? "-"} cm</span>
        </div>
      </div>
    </button>
  );
}