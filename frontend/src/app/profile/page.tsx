"use client";

import { useEffect, useState } from "react";
import { getProfile } from "@/src/services/profile";
import { ProfileResponse } from "@/src/types/profile";

import HeroCard from "@/src/components/profile/HeroCard";
import StatsCards from "@/src/components/profile/StatsCards";
import MatchCard from "@/src/components/profile/MatchCard";
import RoadmapCard from "@/src/components/profile/RoadmapCard";
import AssessmentCard from "@/src/components/profile/AssessmentCard";
import AppLayout from "@/src/components/layout/AppLayout";

export default function ProfilePage() {

    const [profile, setProfile] =
        useState<ProfileResponse | null>(null);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        async function load() {

            try {

                const data = await getProfile();

                setProfile(data);

            } finally {

                setLoading(false);

            }

        }

        load();

    }, []);

    if (loading) {
        return (
            <AppLayout>
                <div className="flex h-[70vh] items-center justify-center">
                    <div className="text-center">
                        <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-blue-600 border-t-transparent"></div>
                        <p className="mt-4 text-gray-500">
                            Loading your career profile...
                        </p>
                    </div>
                </div>
            </AppLayout>
        );
    }

    if (!profile)
        return <p>No profile found.</p>;

    return (
        <AppLayout>
    
            <div className="space-y-8">
    
                <HeroCard
                    profile={profile.profile}
                />
    
                <StatsCards
                    stats={profile.stats}
                />
    
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
    
                    <MatchCard
                        match={profile.latest_match}
                    />
    
                    <RoadmapCard
                        roadmap={profile.roadmap}
                    />
    
                </div>
    
                <AssessmentCard
                    assessment={profile.assessment}
                />
    
            </div>
    
        </AppLayout>
    );

}