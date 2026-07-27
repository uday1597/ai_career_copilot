"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";

import AppLayout from "@/src/components/layout/AppLayout";

import {
    getAssessment,
    generateAssessment,
    submitAssessment,
} from "@/src/services/assessment";

import { Assessment } from "@/src/types/assessment";

import MCQSection from "@/src/components/assessment/MCQCard";
import CodingSection from "@/src/components/assessment/CodingCard";
import ScenarioSection from "@/src/components/assessment/ScenarioCard";
import SubmitAssessmentButton from "@/src/components/assessment/SubmitAssessmentButton";
import { useRouter } from "next/navigation";

export default function AssessmentPage() {
    const router = useRouter();
    const searchParams = useSearchParams();

    const matchId = searchParams.get("matchId");

    const week = Number(
        searchParams.get("week")
    );

    const [assessment, setAssessment] =
        useState<Assessment | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [mcqAnswers, setMcqAnswers] =
        useState<number[]>([]);

    const [codingAnswers, setCodingAnswers] =
        useState<string[]>([]);

    const [scenarioAnswer, setScenarioAnswer] =
        useState("");
    const [submitting, setSubmitting] =
        useState(false);

    useEffect(() => {

        if (!matchId || !week) return;

        loadAssessment();

    }, [matchId, week]);

    async function loadAssessment() {

        if (!matchId || !week) return;

        setLoading(true);

        try {

            const result =
                await getAssessment(
                    matchId,
                    week
                );

            setAssessment(result);

        } catch {

            const generated =
                await generateAssessment(
                    matchId,
                    week
                );

            setAssessment(generated);

        } finally {

            setLoading(false);

        }

    }

    async function handleSubmit() {

        if (!assessment) return;
    
        setSubmitting(true);
    
        try {
            console.log({
                assessment_id: assessment.id,
                mcq_answers: mcqAnswers,
                coding_answers: codingAnswers,
                scenario_answer: scenarioAnswer,
            });
            const result = await submitAssessment(
                assessment.id,
                mcqAnswers,
                codingAnswers,
                scenarioAnswer
            );
    
            // Later:
            router.push(`/assessment/result?id=${assessment.id}`);
    
        } catch (error) {
    
            console.error(error);
    
            alert("Failed to submit assessment.");
    
        } finally {
    
            setSubmitting(false);
    
        }
    
    }

    if (loading) {

        return (

            <AppLayout>

                <div className="rounded-xl border bg-white p-10 text-center">

                    Loading Assessment...

                </div>

            </AppLayout>

        );

    }

    if (!assessment) {

        return (

            <AppLayout>

                <div className="rounded-xl border bg-white p-10 text-center">

                    Assessment could not be loaded.

                </div>

            </AppLayout>

        );

    }

    return (

        <AppLayout>

            <div className="space-y-8">

                <div className="rounded-xl border bg-white p-6 shadow-sm">

                    <h1 className="text-3xl font-bold">

                        {assessment.questions.title}

                    </h1>

                    <div className="mt-4 flex gap-6 text-slate-600">

                        <p>
                            Week {assessment.week}
                        </p>

                        <p>
                            {assessment.questions.difficulty}
                        </p>

                        <p>
                            {assessment.questions.estimated_duration}
                        </p>

                    </div>

                </div>

                <div className="space-y-6">

                    {assessment.questions.mcqs.map((question, index) => (

                        <MCQSection
                            key={question.id}
                            question={question}
                            selected={
                                mcqAnswers[index] ?? null
                            }
                            onSelect={(selectedOption) => {

                                const updated = [...mcqAnswers];

                                updated[index] = selectedOption;

                                setMcqAnswers(updated);

                            }}
                        />

                    ))}

                </div>

                <div className="space-y-6">

                    {assessment.questions.coding.map((question, index) => (

                        <CodingSection
                            key={question.id}
                            question={question}
                            answer={codingAnswers[index] ?? ""}
                            onChange={(value) => {

                                const updated = [...codingAnswers];

                                updated[index] = value;

                                setCodingAnswers(updated);

                            }}
                        />

                    ))}

                </div>

                <ScenarioSection
                    question={assessment.questions.scenario[0]}
                    answer={scenarioAnswer}
                    onChange={setScenarioAnswer}
                />

                <div className="flex justify-end">

                <SubmitAssessmentButton
                    loading={submitting}
                    onClick={handleSubmit}
                />

                </div>

            </div>

        </AppLayout>

    );

}