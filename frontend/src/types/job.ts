export interface Job {

    id: string;

    title: string;

    company: string;

    location: string;

    technologies: string[];

    match_score?: number;

}