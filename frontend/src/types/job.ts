export interface Job {

    id: string;

    title: string;

    company: string;

    location: string | null;

    description: string;

    technologies: string[];

    match_score?: number;

}