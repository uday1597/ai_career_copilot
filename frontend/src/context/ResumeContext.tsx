"use client";

import {
    createContext,
    useContext,
    useEffect,
    useState,
    ReactNode,
} from "react";

import { Resume } from "../types/resume";

interface ResumeContextType {
    resume: Resume | null;
    hydrated: boolean;
    setResume: (resume: Resume | null) => void;
    clearResume: () => void;
}

const ResumeContext = createContext<
    ResumeContextType | undefined
>(undefined);

export function ResumeProvider({
    children,
}: {
    children: ReactNode;
}) {

    const [resume, setResumeState] =
        useState<Resume | null>(null);

    const [hydrated, setHydrated] =
        useState(false);

    useEffect(() => {

        const stored =
            localStorage.getItem("resume");

        if (stored) {
            setResumeState(
                JSON.parse(stored)
            );
        }

        setHydrated(true);

    }, []);

    function setResume(
        resume: Resume | null
    ) {

        setResumeState(resume);

        if (resume) {
            localStorage.setItem(
                "resume",
                JSON.stringify(resume)
            );
        } else {
            localStorage.removeItem("resume");
        }

    }

    function clearResume() {

        setResumeState(null);

        localStorage.removeItem("resume");

    }

    return (

        <ResumeContext.Provider
            value={{
                resume,
                hydrated,
                setResume,
                clearResume,
            }}
        >
            {children}
        </ResumeContext.Provider>

    );

}

export function useResume() {

    const context =
        useContext(ResumeContext);

    if (!context) {
        throw new Error(
            "useResume must be used inside ResumeProvider"
        );
    }

    return context;

}