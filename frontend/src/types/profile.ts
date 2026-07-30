export interface ProfileSummary {
    resume_filename: string;
    summary: string | null;
    skills: string[];
    resume_uploaded_at: string | null;
}

export interface CareerStats {
    resumes: number;
    jobs: number;
    matches: number;
    roadmaps: number;
    assessments: number;
}

export interface LatestMatch {
    job_title: string;
    company: string;
    match_score: number;
    missing_skills: string[];
}

export interface RoadmapSummary {
    current_week: number;
    completed_weeks: number;
    total_weeks: number;
    progress: number;
}

export interface AssessmentSummary {
    completed: number;
    average_score: number;
    highest_score: number;
}

export interface ProfileResponse {
    profile: ProfileSummary;
    stats: CareerStats;
    latest_match: LatestMatch | null;
    roadmap: RoadmapSummary | null;
    assessment: AssessmentSummary;
}