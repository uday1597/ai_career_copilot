import api from "./api";

export async function matchResume(
    resumeId: string,
    jobId: string
) {
    const response = await api.post("/analysis/match", {
        resume_id:resumeId,
        job_id:jobId,
    });

    return response.data;
}