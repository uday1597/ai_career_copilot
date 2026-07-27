"use client";

import { useState } from "react";

import AppLayout from "../../components/layout/AppLayout";

import JobSearch from "../../components/jobs/JobSearch";
import JobList from "../../components/jobs/JobList";
import PostJobForm from "../../components/jobs/PostJobForm";

import { discoverJobs } from "../../services/jobs";

import { Job } from "../../types/job";

import { useResume } from "../../hooks/useResume";
import ResumePreview from "../../components/resume/ResumePreview";

type Tab = "discover" | "post";

export default function JobsPage() {

    const { resume } = useResume();

    const [activeTab, setActiveTab] =
        useState<Tab>("discover");

    const [jobs, setJobs] =
        useState<Job[]>([]);

    async function handleDiscoverJobs() {

        const result =
            await discoverJobs();

        setJobs(result);

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

                    <ResumePreview
                        resume={resume}
                    />

                )}

                <div className="flex border-b">

                    <button
                        onClick={() =>
                            setActiveTab("discover")
                        }
                        className={`px-6 py-3 font-medium transition

                            ${
                                activeTab === "discover"
                                    ? "border-b-2 border-indigo-600 text-indigo-600"
                                    : "text-slate-500 hover:text-slate-800"
                            }
                        `}
                    >

                        Discover Jobs

                    </button>

                    <button
                        onClick={() =>
                            setActiveTab("post")
                        }
                        className={`px-6 py-3 font-medium transition

                            ${
                                activeTab === "post"
                                    ? "border-b-2 border-indigo-600 text-indigo-600"
                                    : "text-slate-500 hover:text-slate-800"
                            }
                        `}
                    >

                        Post a Job

                    </button>

                </div>

                {activeTab === "discover" && (

                    <div className="space-y-6">

                        <JobSearch
                            onSearch={handleDiscoverJobs}
                        />

                        <JobList
                            jobs={jobs}
                        />

                    </div>

                )}

                {activeTab === "post" && (

                    <PostJobForm />

                )}

            </div>

        </AppLayout>

    );

}