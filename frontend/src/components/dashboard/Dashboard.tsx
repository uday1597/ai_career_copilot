"use client";

import { useEffect, useState } from "react";

import AppLayout from "@/src/components/layout/AppLayout";

import { Dashboard } from "@/src/types/dashboard";

import { getDashboard } from "@/src/services/dashboard";

import DashboardHeader from "@/src/components/dashboard/DashboardHeader";
import MatchCard from "@/src/components/dashboard/MatchCard";
import RoadmapProgressCard from "@/src/components/dashboard/RoadmapProgressCard";
import AssessmentSummaryCard from "@/src/components/dashboard/AssessmentSummaryCard";
import SkillsCard from "@/src/components/dashboard/SkillsCard";

export default function DashboardPage() {

    const [dashboard, setDashboard] =
        useState<Dashboard | null>(null);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        loadDashboard();

    }, []);

    async function loadDashboard() {

        try {

            const result =
                await getDashboard();

            setDashboard(result);

        }

        finally {

            setLoading(false);

        }

    }

    if (loading) {

        return (

            <AppLayout>

                <div className="rounded-xl border bg-white p-10 text-center">

                    Loading Dashboard...

                </div>

            </AppLayout>

        );

    }

    if (!dashboard) {

        return (

            <AppLayout>

                <div className="rounded-xl border bg-white p-10 text-center">

                    Dashboard unavailable.

                </div>

            </AppLayout>

        );

    }

    return (

        <AppLayout>

            <div className="space-y-6">

                <DashboardHeader />

                <div className="grid gap-6 md:grid-cols-2">

                    <MatchCard
                        match={dashboard.latest_match}
                    />

                    <RoadmapProgressCard
                        roadmap={dashboard.roadmap}
                    />

                </div>

                <div className="grid gap-6 md:grid-cols-2">

                    <AssessmentSummaryCard
                        assessment={
                            dashboard.assessments
                        }
                    />

                    <SkillsCard
                        skills={dashboard.skills}
                    />

                </div>

            </div>

        </AppLayout>

    );

}