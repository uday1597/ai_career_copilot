export interface LatestMatch {
    job_title: string | null;
    company: string | null;
    match_score: number | null;
  }

export interface RoadmapSummary {

    total_weeks: number;

    completed_weeks: number;

    in_progress_weeks: number;

    not_started_weeks: number;

    completion_percentage: number;

}

export interface AssessmentSummary {

    attempted: number;

    average_score: number;

    best_score: number;

}

export interface SkillSummary {

    strongest: string[];

    weakest: string[];

}

export interface Dashboard {

    latest_match: LatestMatch;

    roadmap: RoadmapSummary;

    assessments: AssessmentSummary;

    skills: SkillSummary;

}