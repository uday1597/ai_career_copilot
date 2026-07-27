import api from "./api";

export async function generateAssessment(
    matchId: string,
    week: number,
) {

    const response = await api.post(
        "/assessment/generate",
        {
            match_id: matchId,
            week,
        }
    );

    return response.data;

}

export async function getAssessment(
    matchId: string,
    week: number,
) {

    const response = await api.get(
        `/assessment/${matchId}/${week}`
    );

    return response.data;

}

export async function submitAssessment(
    assessmentId: string,
    mcqAnswers: number[],
    codingAnswers: string[],
    scenarioAnswer: string,
) {

    const response = await api.post(
        "/assessment/submit",
        {
            assessment_id: assessmentId,
            mcq_answers: mcqAnswers,
            coding_answers: codingAnswers,
            scenario_answer: scenarioAnswer,
        }
    );

    return response.data;

}

export async function getAssessmentResult(
    id: string
) {

    const response =
        await api.get(
            `/assessment/result/${id}`
        );

    return response.data;

}

export async function getAssessmentHistory(
    matchId: string
) {

    const response =
        await api.get(
            `/assessment/match/${matchId}`
        );

    return response.data;

}

export async function getAssessmentStatus(
    matchId: string,
    week: number,
) {
    const response = await api.get(
        `/assessment/status/${matchId}/${week}`
    );

    return response.data;
}

export async function createNewAssessment(
    matchId: string,
    week: number,
) {
    const response = await api.post(
        "/assessment/new-attempt",
        {
            match_id: matchId,
            week,
        }
    );

    return response.data;
}