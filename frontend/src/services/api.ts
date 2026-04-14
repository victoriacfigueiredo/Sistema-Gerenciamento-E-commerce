import axios from "axios";
import type { Product, ProductDetails, ProductFormData } from "../types/product";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function getProducts(skip = 0, limit = 12) {
  const response = await api.get<Product[]>(`/produtos/?skip=${skip}&limit=${limit}`);
  return response.data;
}

export async function searchProducts(query: string, skip = 0, limit = 12) {
  const response = await api.get<Product[]>(
    `/produtos/busca?q=${encodeURIComponent(query)}&skip=${skip}&limit=${limit}`
  );
  return response.data;
}

export async function getProductDetails(id: string) {
  const response = await api.get<ProductDetails>(`/produtos/${id}/detalhes`);
  return response.data;
}

export async function createProduct(payload: ProductFormData) {
  const response = await api.post<Product>("/produtos/", payload);
  return response.data;
}

export async function updateProduct(
  id: string,
  payload: Omit<ProductFormData, "id_produto">
) {
  const response = await api.put<Product>(`/produtos/${id}`, payload);
  return response.data;
}

export async function deleteProduct(id: string) {
  await api.delete(`/produtos/${id}`);
}

export default api;