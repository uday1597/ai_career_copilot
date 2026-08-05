import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

console.log("✅ API_URL =", API_URL);

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  return config;
});

export default api;