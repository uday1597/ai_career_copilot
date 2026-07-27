"use client";

import { useEffect, useState } from "react";

import AppLayout from "../../components/layout/AppLayout";

import { useMatch } from "../../context/MatchContext";

import { LearningRoadmap } from "@/src/types/roadMap";

import {
    getRoadmap,
    generateRoadmap,
} from "@/src/services/roadmap";

import RoadmapHeader from "@/src/components/roadmap/RoadmapHeader";
import GenerateRoadmapButton from "@/src/components/roadmap/GenerateRoadMapButton";
import LearningTimeline from "@/src/components/roadmap/LearningTimeline";
import {
    getAssessmentHistory,
} from "@/src/services/assessment";

import {
    AssessmentHistory,
} from "@/src/types/assessmentHistory";
import { useRouter } from "next/navigation";

import {
    getAssessmentStatus,
    createNewAssessment,
} from "@/src/services/assessment";

import AssessmentChoiceDialog from "@/src/components/assessment/AssessmentChoiceDialog";

export default function RoadmapPage() {

    const { matchResult } = useMatch();
    const router = useRouter();
    const [roadmap, setRoadmap] =
        useState<LearningRoadmap | null>(null);

    const [loading, setLoading] =
        useState(false);
    const [dialogOpen, setDialogOpen] =
        useState(false);
    
    const [selectedWeek, setSelectedWeek] =
        useState(0);
    
    const [assessmentStatus, setAssessmentStatus] =
        useState<any>(null);
    const [
        history,
        setHistory,
    ] = useState<
        AssessmentHistory[]
    >([]);
    useEffect(() => {

        if (!matchResult)
            return;
    
        loadRoadmap();
    
        loadHistory();
    
    }, [matchResult]);
    
    async function loadHistory() {
    
        if (!matchResult)
            return;
    
        const result =
            await getAssessmentHistory(
                matchResult.id
            );
    
        setHistory(result);
    
    }
    async function handleTakeAssessment(
        week: number
    ) {
    
        if (!matchResult) return;
    
        const status =
            await getAssessmentStatus(
                matchResult.id,
                week
            );
    
        if (!status.exists) {
    
            router.push(
                `/assessment?matchId=${matchResult.id}&week=${week}`
            );
    
            return;
    
        }
    
        setSelectedWeek(week);
    
        setAssessmentStatus(status);
    
        setDialogOpen(true);
    
    }
    function continueAssessment() {

        router.push(
            `/assessment?matchId=${matchResult!.id}&week=${selectedWeek}`
        );
    
    }
    async function newAttempt() {

        await createNewAssessment(
            matchResult!.id,
            selectedWeek
        );
    
        router.push(
            `/assessment?matchId=${matchResult!.id}&week=${selectedWeek}`
        );
    
    }
    useEffect(() => {

        if (!matchResult) {
            return;
        }

        loadRoadmap();

    }, [matchResult]);

    async function loadRoadmap() {

        if (!matchResult) return;

        try {

            const result = await getRoadmap(
                matchResult.id
            );

            setRoadmap(result.roadmap);

        } catch {

            // No roadmap exists yet.
            // User can generate one.

        }

    }

    async function handleGenerateRoadmap() {

        if (!matchResult) return;

        setLoading(true);
        try {

            const result = await generateRoadmap(
                matchResult.id
            );

            setRoadmap(result.roadmap);

        } finally {

            setLoading(false);

        }

    }

    return (

        <AppLayout>

            <div className="space-y-6">

                <RoadmapHeader
                    score={matchResult?.match_score ?? 0}
                />

                {matchResult && (

                    <div className="rounded-xl border bg-white p-6 shadow-sm">

                        <h2 className="text-lg font-semibold">
                            AI Career Recommendation
                        </h2>

                        <p className="mt-3 text-slate-600">
                            {matchResult.ai_explanation.summary}
                        </p>

                    </div>

                )}

                {!roadmap && (

                    <GenerateRoadmapButton
                        loading={loading}
                        onClick={handleGenerateRoadmap}
                    />

                )}

                {roadmap && matchResult && (
                    <LearningTimeline
                        roadmap={roadmap}
                        history={history}
                        onTakeAssessment={handleTakeAssessment}
                    />
                )}
                <AssessmentChoiceDialog
                    open={dialogOpen}
                    status={assessmentStatus?.status ?? ""}
                    previousScore={
                        assessmentStatus?.overall_score
                    }
                    onContinue={continueAssessment}
                    onNew={newAttempt}
                    onClose={() =>
                        setDialogOpen(false)
                    }
                />
            </div>

        </AppLayout>

    );

}