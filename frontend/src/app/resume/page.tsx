"use client";

import ResumeUpload from "../../components/resume/ResumeUpload";
import ResumeSummary from "../../components/resume/ResumeSummary";
import TechnologyList from "../../components/resume/TechnologyList";

import { useResume } from "../../hooks/useResume";
import ResumePreview from "@/src/components/resume/ResumePreview";

export default function ResumePage() {

    const { resume, setResume } = useResume();

    return (
        <div className="p-6 lg:p-8">
            <div className="space-y-6">
                {resume && (
                    <ResumePreview resume={resume} />
                )}
                <ResumeUpload
                    onUpload={setResume}
                />

                {resume && (
                    <ResumeSummary
                        resume={resume}
                    />
                )}

                {resume && (
                    <TechnologyList
                        resume={resume}
                    />
                )}

            </div>
        </div>
    );
}