"use client";

import { useState } from "react";

import AppLayout from "../../components/layout/AppLayout";
import JobSearch from "../../components/jobs/JobSearch";
import JobList from "../../components/jobs/JobList";
import PostJobForm from "../../components/jobs/PostJobForm";
import ResumePreview from "../../components/resume/ResumePreview";

import { discoverJobs } from "../../services/jobs";
import { CrawledJob } from "../../types/job";
import { useResume } from "../../hooks/useResume";

type Tab = "discover" | "post";

export default function JobsPage() {
    const { resume } = useResume();

    const [activeTab, setActiveTab] = useState<Tab>("post");

    const [jobs, setJobs] = useState<CrawledJob[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleDiscoverJobs() {
        try {
            setLoading(true);
            setError("");

            const result = await discoverJobs();
            setJobs(result);
        } catch (err) {
            console.error(err);
            setError("Failed to discover jobs.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <AppLayout>
            <div className="space-y-6">
                <div>
                    <h1 className="text-3xl font-bold">
                        Jobs
                    </h1>

                    <p className="mt-2 text-slate-600">
                        Discover AI-powered job recommendations or post your own opportunity.
                    </p>
                </div>

                {resume && (
                    <ResumePreview resume={resume} />
                )}

                <div className="flex border-b">
                    <button
                        onClick={() => setActiveTab("post")}
                        className={`px-6 py-3 font-medium transition ${
                            activeTab === "post"
                                ? "border-b-2 border-indigo-600 text-indigo-600"
                                : "text-slate-500 hover:text-slate-800"
                        }`}
                    >
                        Post a Job
                    </button>
                    <button
                        onClick={() => setActiveTab("discover")}
                        className={`px-6 py-3 font-medium transition ${
                            activeTab === "discover"
                                ? "border-b-2 border-indigo-600 text-indigo-600"
                                : "text-slate-500 hover:text-slate-800"
                        }`}
                    >
                        Discover Jobs
                    </button>
                </div>

                {activeTab === "discover" && (
                    <div className="space-y-6">
                        <JobSearch
                            onSearch={handleDiscoverJobs}
                        />

                        {loading && (
                            <div className="rounded-lg border bg-white p-6 text-center">
                                Loading jobs...
                            </div>
                        )}

                        {error && (
                            <div className="rounded-lg border border-red-200 bg-red-50 p-4 text-red-700">
                                {error}
                            </div>
                        )}

                        {!loading && !error && (
                            <JobList jobs={jobs} />
                        )}
                    </div>
                )}

                {activeTab === "post" && (
                    <PostJobForm />
                )}
            </div>
        </AppLayout>
    );
}