import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://127.0.0.1:8000/api", // Укажи URL к вашему API
    headers: {
        "Content-Type": "application/json",
    },
});

// Перехватчик для добавления токена в заголовки
apiClient.interceptors.request.use((config) => {
    const token = localStorage.getItem("token"); // Токен хранится в localStorage
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default {
    // Получить список проектов
    getProjects() {
        return apiClient.get("/projects/");
    },

    // Получить список терминов для проекта
    getTerms(projectId) {
        return apiClient.get(`/projects/${projectId}/terms/`);
    },

    // Добавить новый термин
    createTerm(projectId, termData) {
        return apiClient.post(`/projects/${projectId}/terms/`, termData);
    },

    // Обновить термин
    updateTerm(projectId, termId, termData) {
        return apiClient.put(`/projects/${projectId}/terms/${termId}/`, termData);
    },

    // Удалить термин
    deleteTerm(projectId, termId) {
        return apiClient.delete(`/projects/${projectId}/terms/${termId}/`);
    },

    // Регистрация пользователя
    register(credentials) {
        return apiClient.post("/register/", credentials);
    },
};