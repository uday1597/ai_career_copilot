"use client";

interface MatchButtonProps {
    disabled: boolean;
    loading: boolean;
    onClick: () => void;
}

export default function MatchButton({
    disabled,
    loading,
    onClick,
}: MatchButtonProps) {

    return (
        <button
            disabled={disabled || loading}
            onClick={onClick}
            className="rounded-lg bg-blue-600 px-6 py-3 text-white disabled:cursor-not-allowed disabled:bg-slate-400"
        >
            {loading ? "Matching..." : "Match Resume"}
        </button>
    );
}