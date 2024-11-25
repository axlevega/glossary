<template>
    <div>
      <h1>Термины проекта: {{ projectId }}</h1>
      <ul>
        <li v-for="term in terms" :key="term.id">
          <strong>{{ term.word }}</strong>: {{ term.definition }}
          <button @click="editTerm(term)">Редактировать</button>
          <button @click="deleteTerm(term.id)">Удалить</button>
        </li>
      </ul>
  
      <!-- Форма добавления или редактирования -->
      <form @submit.prevent="saveTerm">
        <h2>{{ isEditing ? "Редактировать" : "Добавить новый" }} термин</h2>
        <label>
          Слово:
          <input v-model="currentTerm.word" type="text" required />
        </label>
        <label>
          Определение:
          <textarea v-model="currentTerm.definition" required></textarea>
        </label>
        <button type="submit">
          {{ isEditing ? "Сохранить изменения" : "Добавить" }}
        </button>
        <button type="button" @click="cancelEdit" v-if="isEditing">Отмена</button>
      </form>
    </div>
  </template>
  
  <script>
  import apiService from "../services/apiService";
  
  export default {
    data() {
      return {
        projectId: this.$route.params.id,
        terms: [], // Список терминов
        currentTerm: {
          id: null,
          word: "",
          definition: "",
        },
        isEditing: false, // Флаг для редактирования
      };
    },
    methods: {
      async fetchTerms() {
        try {
          const response = await apiService.getTerms(this.projectId);
          this.terms = response.data;
        } catch (error) {
          console.error("Ошибка при загрузке терминов:", error);
        }
      },
      async saveTerm() {
        try {
          if (this.isEditing) {
            await apiService.updateTerm(this.projectId, this.currentTerm.id, this.currentTerm);
          } else {
            await apiService.createTerm(this.projectId, this.currentTerm);
          }
          this.resetForm();
          this.fetchTerms();
        } catch (error) {
          console.error("Ошибка при сохранении термина:", error);
        }
      },
      editTerm(term) {
        this.currentTerm = { ...term }; // Копируем данные термина
        this.isEditing = true;
      },
      async deleteTerm(termId) {
        try {
          await apiService.deleteTerm(this.projectId, termId);
          this.fetchTerms(); // Обновляем список
        } catch (error) {
          console.error("Ошибка при удалении термина:", error);
        }
      },
      cancelEdit() {
        this.resetForm();
      },
      resetForm() {
        this.currentTerm = {
          id: null,
          word: "",
          definition: "",
        };
        this.isEditing = false;
      },
    },
    mounted() {
      this.fetchTerms();
    },
  };
  </script>
  
  <style>
  /* Добавь стили, если нужно */
  </style>
  