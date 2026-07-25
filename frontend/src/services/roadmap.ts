import api from "./api";

export async function generateRoadmap(
    matchId: string
) {
    const response = await api.post(
        "/roadmap/generate",
        {
            match_id: matchId,
        }
    );

    return response.data;
}

export async function getRoadmap(
    matchId: string
) {
    const response = await api.get(
        `/roadmap/${matchId}`
    );

    return response.data;
}