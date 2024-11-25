<template>
    <div>
      <h1>Вход</h1>
      <form @submit.prevent="login">
        <label>
          Имя пользователя:
          <input v-model="credentials.username" type="text" required />
        </label>
        <label>
          Пароль:
          <input v-model="credentials.password" type="password" required />
        </label>
        <button type="submit">Войти</button>
      </form>
      <p v-if="error" style="color: red;">Ошибка входа: {{ error }}</p>
      <p>
        Нет аккаунта? <router-link to="/register">Зарегистрируйтесь</router-link>.
      </p>
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
  
      const login = async () => {
        try {
          const response = await apiService.login(credentials);
          localStorage.setItem("token", response.data.access); // Сохраняем токен
          router.push("/"); // Перенаправляем на главную страницу
        } catch (err) {
          error.value = "Неверное имя пользователя или пароль.";
          console.error("Ошибка входа:", err);
        }
      };
  
      return {
        credentials,
        error,
        login,
      };
    },
  };
  </script>
  
  <style>
  /* Добавь стили, если нужно */
  </style>
  