"use client";

import { useEffect, useState } from "react";
import AppLayout from "../../components/layout/AppLayout";
import CurrentResume from "../../components/resume/CurrentResume";
import JobDropdown from "../../components/match/JobDropdown";
import ResumeDropdown from "../../components/match/ResumeDropdown";
import { getJobs } from "../../services/jobs";
import { Job } from "../../types/job";
import { useResume } from "../../hooks/useResume";
import MatchButton from "../../components/match/MatchButton";
import { matchResume } from "../../services/match";
import MatchScoreCard from "../../components/match/MatchScoreCard";
import MatchingSkills from "../../components/match/MatchingSkills";
import MissingSkills from "../../components/match/MissingSkills";
import AIMatchExplanation from "@/src/components/match/AIMatchExplanation";
import MatchRecommendation from "@/src/components/match/MatchRecommendation";
import { Resume } from "@/src/types/resume";
import { getResumes } from "@/src/services/resume";
import ResumePreview from "@/src/components/resume/ResumePreview";
import { useMatch } from "../../context/MatchContext";

export default function MatchPage() {

    const [jobs, setJobs] = useState<Job[]>([]);
    const [resumes, setResumes] = useState<Resume[]>([]);

    const [selectedJobId, setSelectedJobId] = useState("");
    const [selectedResumeId, setSelectedResumeId] = useState("");

    const { resume } = useResume();

    const [loading, setLoading] = useState(false);

    const {
        matchResult,
        setMatchResult,
    } = useMatch();

    useEffect(() => {
            loadJobs();
            loadResumes();
        }, []);

    async function loadJobs() {
        const result = await getJobs();
        setJobs(result);
    }
    async function loadResumes() {
        const result = await getResumes();
        setResumes(result);
    }

    async function handleMatch() {
        const resumeToUse = selectedResumeId
            ? resumes.find(r => r.id === selectedResumeId)
            : resume;
    
        if (!resumeToUse || !selectedJobId) return;
    
        setLoading(true);
    
        try {
            const result = await matchResume(
                resumeToUse.id,
                selectedJobId
            );
    
            setMatchResult(result);
        } finally {
            setLoading(false);
        }
    }

    return (
        <AppLayout>

            <div className="space-y-6">

            <div className="grid gap-6">

                {/* First row */}
                {resume && (
                    <ResumePreview resume={resume} />
                )}

                {/* Second row */}
                <div className="grid gap-6 lg:grid-cols-2">
                    <ResumeDropdown
                        resumes={resumes}
                        selectedResumeId={selectedResumeId}
                        onChange={setSelectedResumeId}
                    />

                    <JobDropdown
                        jobs={jobs}
                        selectedJobId={selectedJobId}
                        onChange={setSelectedJobId}
                    />
                </div>

            </div>

                <div className="flex justify-center">

                <MatchButton
                    disabled={
                        !(selectedResumeId || resume) ||
                        !selectedJobId
                    }
                    loading={loading}
                    onClick={handleMatch}
                />

                </div>

                {matchResult && (

                    <div className="mt-8 space-y-6">

                        {/* Row 1 */}

                        <div className="grid gap-6 lg:grid-cols-2">

                            <MatchScoreCard
                                score={matchResult.match_score}
                            />

                            <MatchingSkills
                                skills={matchResult.matching_technologies}
                            />

                        </div>

                        {/* Row 2 */}

                        <div className="grid gap-6 lg:grid-cols-2">

                            <MissingSkills
                                skills={matchResult.missing_technologies}
                            />

                            <MatchRecommendation
                                score={matchResult.match_score}
                            />

                        </div>

                        {/* Row 3 */}

                        <AIMatchExplanation
                            explanation={matchResult.ai_explanation}
                        />

                    </div>

                    )}
            </div>

        </AppLayout>
    );
}