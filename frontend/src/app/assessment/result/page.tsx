"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";

import AppLayout from "@/src/components/layout/AppLayout";

import { getAssessmentResult } from "@/src/services/assessment";

import { Assessment } from "@/src/types/assessment";

import ScoreCard from "@/src/components/assessment/result/ScoreCard";
import StrengthCard from "@/src/components/assessment/result/StrengthCard";
import WeaknessCard from "@/src/components/assessment/result/WeaknessCard";
import FeedbackCard from "@/src/components/assessment/result/FeedbackCard";
import NextStepCard from "@/src/components/assessment/result/NextStepCard";

export default function AssessmentResultPage() {

    const params = useSearchParams();

    const id = params.get("id");

    const [assessment, setAssessment] =
        useState<Assessment | null>(null);

    useEffect(() => {

        if (!id) return;

        load();

    }, [id]);

    async function load() {

        if (!id) return;

        const result =
            await getAssessmentResult(id);

        setAssessment(result);

    }

    if (!assessment) {

        return (

            <AppLayout>

                Loading...

            </AppLayout>

        );

    }

    return (

        <AppLayout>

            <div className="space-y-6">

                <ScoreCard
                    assessment={assessment}
                />

                <div className="grid gap-6 lg:grid-cols-2">

                    <StrengthCard
                        strengths={
                            assessment.feedback.strengths
                        }
                    />

                    <WeaknessCard
                        weaknesses={
                            assessment.feedback.weaknesses
                        }
                    />

                </div>

                <FeedbackCard
                    summary={
                        assessment.feedback.summary
                    }
                />

                <NextStepCard
                    nextAction={
                        assessment.feedback.next_action
                    }
                />

            </div>

        </AppLayout>

    );

}