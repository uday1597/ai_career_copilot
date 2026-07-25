import api from "./api";

export async function getJobs() {
    const response = await api.get("/jobs");
    return response.data;
}

export async function discoverJobs() {

    const response = await api.get(
        "/job-discovery/search"
    );

    return response.data;

}

export async function matchCapabilities() {

    const response = await api.get(
        "/jobs/{job_id}/match?resume_id={resume_id}"
    );

    return response.data;

}