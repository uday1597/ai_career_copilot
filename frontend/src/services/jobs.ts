import { CrawledJob } from "../types/job";
import api from "./api";

export async function getJobs() {
    const response = await api.get("/jobs");
    return response.data;
}


export async function discoverJobs(): Promise<CrawledJob[]> {
    const response = await api.get<CrawledJob[]>(
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