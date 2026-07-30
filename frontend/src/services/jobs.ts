import api from "./api";

export async function getJobs() {

    console.log("Base URL:", api.defaults.baseURL);
    console.log("Endpoint:", "/jobs");
    console.log("Final URL:", `${api.defaults.baseURL}/jobs`);
    
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

export async function createJob(
    job: {
        title: string;
        company: string;
        location: string;
        description: string;
    }
) {

    const response = await api.post(
        "/jobs",
        job
    );

    return response.data;

}