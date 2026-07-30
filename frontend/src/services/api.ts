import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

console.log("✅ API_URL =", API_URL);

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {

  console.log("========== AXIOS REQUEST ==========");
  console.log(config);
  console.log(config.baseURL);
  console.log(JSON.stringify(config, null, 2));
  console.log("==================================");
  return config;
});

export default api;