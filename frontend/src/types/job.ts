export interface Job {

    id: string;

    title: string;

    company: string;

    location: string | null;

    description: string;

    technologies: string[];

    match_score?: number;

}

export interface CrawledJob {
    title: string;
    company: string;
    location: string;
    department?: string;
    job_id: string;
    url: string;
}