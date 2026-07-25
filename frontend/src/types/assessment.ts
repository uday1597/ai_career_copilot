export interface MCQ {

    id: number;

    question: string;

    options: string[];

    answer: number;

    explanation: string;

}

export interface CodingQuestion {

    id: number;

    title: string;

    question: string;

    difficulty: string;

    expected_skills: string[];

    hints: string[];

}

export interface ScenarioQuestion {

    id: number;

    question: string;

    expected_points: string[];

    sample_answer: string;

}

export interface AssessmentQuestions {

    title: string;

    estimated_duration: string;

    difficulty: string;

    mcqs: MCQ[];

    coding: CodingQuestion[];

    scenario: ScenarioQuestion[];

}

export interface Assessment {

    id: string;

    match_id: string;

    week: number;

    questions: AssessmentQuestions;

    mcq_score: number;

    coding_score: number;

    scenario_score: number;

    overall_score: number;

    status: string;

    feedback: {

        strengths: string[];

        weaknesses: string[];

        recommendations: string[];

        summary: string;

        next_action: string;

    };

}