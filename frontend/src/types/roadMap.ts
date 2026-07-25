export interface Week {

    week: number;

    focus: string;

    topics: string[];

    mini_project: string;

    resources: string[];

}

export interface LearningRoadmap {

    estimated_completion: string;

    weeks: Week[];

}