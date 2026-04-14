export interface Product {
  id_produto: string;
  nome_produto: string;
  categoria_produto: string;
  peso_produto_gramas: number | null;
  comprimento_centimetros: number | null;
  altura_centimetros: number | null;
  largura_centimetros: number | null;
}

export interface Review {
  id_avaliacao: string;
  id_pedido: string;
  avaliacao: number;
  titulo_comentario: string | null;
  comentario: string | null;
  data_comentario: string | null;
  data_resposta: string | null;
}

export interface ProductMetrics {
  total_vendas: number;
  faturamento_total: number;
  total_avaliacoes: number;
  media_avaliacoes: number | null;
}

export interface ProductDetails extends Product {
  metricas: ProductMetrics;
  avaliacoes: Review[];
}

export interface ProductFormData {
  id_produto: string;
  nome_produto: string;
  categoria_produto: string;
  peso_produto_gramas: number | null;
  comprimento_centimetros: number | null;
  altura_centimetros: number | null;
  largura_centimetros: number | null;
}