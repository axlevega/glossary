<template>
    <div>
      <h1>Регистрация</h1>
      <form @submit.prevent="register">
        <label>
          Имя пользователя:
          <input v-model="credentials.username" type="text" required />
        </label>
        <label>
          Пароль:
          <input v-model="credentials.password" type="password" required />
        </label>
        <button type="submit">Зарегистрироваться</button>
      </form>
      <p v-if="error" style="color: red;">Ошибка регистрации: {{ error }}</p>
    </div>
  </template>
  
  <script>
  import { reactive, ref } from "vue"; // Подключаем reactivity API
  import apiService from "../services/apiService";
  import { useRouter } from "vue-router";
  
  export default {
    setup() {
      const router = useRouter();
      const credentials = reactive({
        username: "",
        password: "",
      });
      const error = ref(null);
  
      const register = async () => {
        try {
          const response = await apiService.register(credentials);
          localStorage.setItem("token", response.data.access); // Сохраняем токен
          router.push("/"); // Перенаправляем на главную страницу
        } catch (err) {
          error.value = "Не удалось зарегистрироваться. Проверьте данные.";
          console.error("Ошибка регистрации:", err);
        }
      };
  
      return {
        credentials,
        error,
        register,
      };
    },
  };
  </script>
  
  <style>
  /* Добавь стили, если нужно */
  </style>
  