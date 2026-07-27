"use client";

interface Props {
    open: boolean;
    status: string;
    previousScore?: number | null;
    onContinue: () => void;
    onNew: () => void;
    onClose: () => void;
}

export default function AssessmentChoiceDialog({
    open,
    status,
    previousScore,
    onContinue,
    onNew,
    onClose,
}: Props) {

    if (!open) return null;

    return (

        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">

            <div className="w-full max-w-lg rounded-xl bg-white p-8 shadow-xl">

                <h2 className="text-2xl font-bold">
                    Assessment Found
                </h2>

                <p className="mt-3 text-slate-600">
                    You already have an assessment for this week.
                </p>

                <div className="mt-6 rounded-lg bg-slate-100 p-4">

                    <p>
                        <strong>Status:</strong> {status}
                    </p>

                    {previousScore != null && (

                        <p className="mt-2">

                            <strong>Previous Score:</strong>{" "}
                            {previousScore}%

                        </p>

                    )}

                </div>

                <div className="mt-8 flex justify-end gap-3">

                    <button
                        onClick={onClose}
                        className="rounded-lg border px-5 py-2"
                    >
                        Cancel
                    </button>

                    <button
                        onClick={onContinue}
                        className="rounded-lg bg-indigo-600 px-5 py-2 text-white"
                    >
                        Continue
                    </button>

                    <button
                        onClick={onNew}
                        className="rounded-lg bg-green-600 px-5 py-2 text-white"
                    >
                        New Attempt
                    </button>

                </div>

            </div>

        </div>

    );

}