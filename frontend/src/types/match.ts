export interface AIExplanation {
    summary: string;
    strengths: string[];
    missing_skills: string[];
    recommendations: string[];
}

export interface MatchResult {

    id: string;

    resume_id: string;

    job_id: string;

    match_score: number;

    matching_technologies: string[];

    missing_technologies: string[];

    ai_explanation: AIExplanation;
}