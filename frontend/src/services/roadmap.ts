import api from "./api";
import { fetchEventSource } from "@microsoft/fetch-event-source";
const API = process.env.NEXT_PUBLIC_API_URL!;

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



export async function generateRoadmapStream(
  matchId: string,
  onEvent: (event: any) => void
) {
  await fetchEventSource(`${API}/roadmap/generate-stream`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      match_id: matchId,
    }),

    async onmessage(msg) {
      if (!msg.data) return;

      onEvent(JSON.parse(msg.data));
    },
  });
}