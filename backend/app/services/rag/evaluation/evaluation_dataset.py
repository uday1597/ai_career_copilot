EVALUATION_DATASET = [

    {
        "id": "missing-skills",
        "question": "What skills are missing for the target job?",
        "expected_sources": [
            "resume",
            "job",
        ],
    },

    {
        "id": "candidate-skills",
        "question": "What technologies does the candidate already know?",
        "expected_sources": [
            "resume",
        ],
    },

    {
        "id": "learning-roadmap",
        "question": "What skills should the candidate learn next?",
        "expected_sources": [
            "resume",
            "job",
            "roadmap",
        ],
    },

    {
        "id": "assessment-performance",
        "question": "What areas did the candidate perform poorly in?",
        "expected_sources": [
            "assessment",
        ],
    },

    {
        "id": "job-requirements",
        "question": "What technologies are required by the target job?",
        "expected_sources": [
            "job",
        ],
    },

]