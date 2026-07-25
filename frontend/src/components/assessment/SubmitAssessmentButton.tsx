interface Props {

    loading: boolean;

    onClick: () => void;

}

export default function SubmitAssessmentButton({

    loading,

    onClick,

}: Props) {

    return (

        <div className="flex justify-end">

            <button

                onClick={onClick}

                disabled={loading}

                className="rounded-lg bg-green-600 px-6 py-3 text-white"

            >

                {loading
                    ? "Submitting..."
                    : "Submit Assessment"}

            </button>

        </div>

    );

}