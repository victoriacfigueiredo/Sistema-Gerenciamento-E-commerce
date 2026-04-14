import { useEffect, useState } from "react";
import type { Product, ProductFormData } from "../types/product";

interface ProductFormProps {
  selectedProduct: Product | null;
  onCreate: (payload: ProductFormData) => Promise<void>;
  onUpdate: (
    id: string,
    payload: Omit<ProductFormData, "id_produto">
  ) => Promise<void>;
  onDelete: (id: string) => Promise<void>;
}

const initialForm: ProductFormData = {
  id_produto: "",
  nome_produto: "",
  categoria_produto: "",
  peso_produto_gramas: null,
  comprimento_centimetros: null,
  altura_centimetros: null,
  largura_centimetros: null,
};

export function ProductForm({
  selectedProduct,
  onCreate,
  onUpdate,
  onDelete,
}: ProductFormProps) {
  const [form, setForm] = useState<ProductFormData>(initialForm);

  useEffect(() => {
    if (selectedProduct) {
      setForm({
        id_produto: selectedProduct.id_produto,
        nome_produto: selectedProduct.nome_produto,
        categoria_produto: selectedProduct.categoria_produto,
        peso_produto_gramas: selectedProduct.peso_produto_gramas,
        comprimento_centimetros: selectedProduct.comprimento_centimetros,
        altura_centimetros: selectedProduct.altura_centimetros,
        largura_centimetros: selectedProduct.largura_centimetros,
      });
    } else {
      setForm(initialForm);
    }
  }, [selectedProduct]);

  function handleChange(field: keyof ProductFormData, value: string) {
    setForm((prev) => ({
      ...prev,
      [field]: [
        "peso_produto_gramas",
        "comprimento_centimetros",
        "altura_centimetros",
        "largura_centimetros",
      ].includes(field)
        ? value === ""
          ? null
          : Number(value)
        : value,
    }));
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    if (selectedProduct) {
      const { id_produto, ...payload } = form;
      await onUpdate(id_produto, payload);
      return;
    }

    await onCreate(form);
    setForm(initialForm);
  }

  return (
    <section className="form-panel">
      <div className="section-card">
        <h3>{selectedProduct ? "Editar produto" : "Adicionar produto"}</h3>

        <form onSubmit={handleSubmit} className="product-form">
          <input
            className="input"
            placeholder="ID do produto"
            value={form.id_produto}
            disabled={!!selectedProduct}
            onChange={(e) => handleChange("id_produto", e.target.value)}
            required
          />

          <input
            className="input"
            placeholder="Nome do produto"
            value={form.nome_produto}
            onChange={(e) => handleChange("nome_produto", e.target.value)}
            required
          />

          <input
            className="input"
            placeholder="Categoria"
            value={form.categoria_produto}
            onChange={(e) => handleChange("categoria_produto", e.target.value)}
            required
          />

          <input
            className="input"
            placeholder="Peso (g)"
            type="number"
            value={form.peso_produto_gramas ?? ""}
            onChange={(e) =>
              handleChange("peso_produto_gramas", e.target.value)
            }
          />

          <input
            className="input"
            placeholder="Comprimento (cm)"
            type="number"
            value={form.comprimento_centimetros ?? ""}
            onChange={(e) =>
              handleChange("comprimento_centimetros", e.target.value)
            }
          />

          <input
            className="input"
            placeholder="Altura (cm)"
            type="number"
            value={form.altura_centimetros ?? ""}
            onChange={(e) =>
              handleChange("altura_centimetros", e.target.value)
            }
          />

          <input
            className="input"
            placeholder="Largura (cm)"
            type="number"
            value={form.largura_centimetros ?? ""}
            onChange={(e) =>
              handleChange("largura_centimetros", e.target.value)
            }
          />

          <div className="form-actions">
            <button type="submit" className="btn btn-primary">
              {selectedProduct ? "Salvar alterações" : "Criar produto"}
            </button>

            {selectedProduct && (
              <button
                type="button"
                className="btn btn-danger"
                onClick={() => onDelete(selectedProduct.id_produto)}
              >
                Remover produto
              </button>
            )}
          </div>
        </form>
      </div>
    </section>
  );
}