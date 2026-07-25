interface Props {
    loading: boolean;
    onClick: () => void;
}

export default function GenerateRoadmapButton({
    loading,
    onClick,
}: Props) {
    return (
        <button
            onClick={onClick}
            className="rounded-lg bg-blue-600 px-6 py-3 text-white"
        >
            {loading ? "Generating..." : "Generate Roadmap"}
        </button>
    );
}