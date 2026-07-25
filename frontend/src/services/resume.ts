import api from "./api";

export async function getResumes() {
    const response = await api.get("/resume");
    return response.data;
}

export function getResumePreviewUrl(resumeId: string) {
    return `${process.env.NEXT_PUBLIC_API_URL}/resume/${resumeId}/preview`;
}

export async function uploadResume(file: File) {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/resume/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}