import api from "./api";

export async function getResumes() {
    console.log("===== getResumes =====");
    console.log("Base URL:", api.defaults.baseURL);
    console.log("Endpoint:", "/resume");
    console.log("Final URL:", `${api.defaults.baseURL}/resume`);
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