"use client";

import {
    createContext,
    useContext,
    useEffect,
    useState,
    ReactNode,
} from "react";

import { MatchResult } from "../types/match";

interface MatchContextType {
    matchResult: MatchResult | null;
    setMatchResult: (result: MatchResult | null) => void;
    clearMatch: () => void;
}

const MatchContext = createContext<MatchContextType | undefined>(
    undefined
);

export function MatchProvider({
    children,
}: {
    children: ReactNode;
}) {

    const [matchResult, setMatchResultState] =
        useState<MatchResult | null>(null);

    const [hydrated, setHydrated] =
        useState(false);

    useEffect(() => {

        const stored =
            localStorage.getItem("matchResult");

        if (stored) {
            setMatchResultState(
                JSON.parse(stored)
            );
        }

        setHydrated(true);

    }, []);

    function setMatchResult(
        result: MatchResult | null
    ) {

        setMatchResultState(result);

        if (result) {

            localStorage.setItem(
                "matchResult",
                JSON.stringify(result)
            );

        } else {

            localStorage.removeItem(
                "matchResult"
            );

        }

    }

    function clearMatch() {

        setMatchResultState(null);

        localStorage.removeItem(
            "matchResult"
        );

    }

    if (!hydrated) {
        return null;
    }

    return (

        <MatchContext.Provider
            value={{
                matchResult,
                setMatchResult,
                clearMatch,
            }}
        >
            {children}
        </MatchContext.Provider>

    );

}

export function useMatch() {

    const context = useContext(MatchContext);

    if (!context) {

        throw new Error(
            "useMatch must be used inside MatchProvider"
        );

    }

    return context;

}