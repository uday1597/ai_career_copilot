
TOOLS = [

    {
        "type": "function",
        "name": "get_dashboard",
        "description": "Returns the user's dashboard.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "search_jobs",
        "description": "Returns available jobs from the Career Copilot database.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_resume_match",
        "description": "Returns the latest resume match analysis including score, matching skills and missing skills.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_learning_roadmap",
        "description": "Returns the user's complete learning roadmap including weeks, topics, focus areas, resources and mini projects.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "get_assessment",
        "description": "Returns assessment results for a specific roadmap week.",
        "parameters": {
            "type": "object",
            "properties": {
                "week": {
                    "type": "integer",
                    "description": "Roadmap week number"
                }
            },
            "required": ["week"]
        }
    }
]