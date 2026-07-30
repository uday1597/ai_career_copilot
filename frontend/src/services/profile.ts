import api from "./api";
import { ProfileResponse } from "../types/profile";

export async function getProfile(): Promise<ProfileResponse> {
    const response = await api.get("/profile");
    return response.data;
}