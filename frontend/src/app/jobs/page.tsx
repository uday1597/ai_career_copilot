"use client";

import { useState } from "react";

import AppLayout from "../../components/layout/AppLayout";

import JobSearch from "../../components/jobs/JobSearch";
import JobList from "../../components/jobs/JobList";

import { discoverJobs } from "../../services/jobs";

import { Job } from "../../types/job";
import { useResume } from "../../hooks/useResume";
import ResumePreview from "../../components/resume/ResumePreview";

export default function JobsPage() {
    const { resume } = useResume();
    const [jobs, setJobs] = useState<Job[]>([]);
    const handleDiscoverJobs = async () => {
        const result = await discoverJobs();
        setJobs(result);
    };

    return (

        <AppLayout>

            <div className="space-y-6">
                {resume && (
                    <ResumePreview resume={resume} />
                )}
                <JobSearch
                    onSearch={handleDiscoverJobs}
                />

                <JobList
                    jobs={jobs}
                />

            </div>

        </AppLayout>

    );

}