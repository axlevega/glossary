<template>
  <div>
    <h1>Мои проекты</h1>
    <ul>
      <li v-for="project in projects" :key="project.id">
        <router-link :to="{ name: 'ProjectDetails', params: { id: project.id } }">
          {{ project.name }}
        </router-link>
      </li>
    </ul>
    <form @submit.prevent="addProject">
      <h2>Добавить новый проект</h2>
      <label>
        Название проекта:
        <input v-model="newProject.name" type="text" required />
      </label>
      <label>
        Домен проекта:
        <input v-model="newProject.domain" type="text" required />
      </label>
      <button type="submit">Добавить</button>
    </form>
  </div>
</template>

<script>
import apiService from "../services/apiService";

export default {
  data() {
    return {
      projects: [], // Список проектов
      newProject: {
        name: "",
        domain: "",
      },
    };
  },
  methods: {
    async fetchProjects() {
      try {
        const response = await apiService.getProjects();
        this.projects = response.data;
      } catch (error) {
        console.error("Ошибка при загрузке проектов:", error);
      }
    },
    async addProject() {
      try {
        await apiService.createProject(this.newProject);
        this.newProject.name = "";
        this.newProject.domain = "";
        this.fetchProjects(); // Обновляем список после добавления
      } catch (error) {
        console.error("Ошибка при добавлении проекта:", error);
      }
    },
  },
  mounted() {
    this.fetchProjects(); // Загружаем проекты при открытии страницы
  },
};
</script>

<style>
/* Добавь стили, если нужно */
</style>
