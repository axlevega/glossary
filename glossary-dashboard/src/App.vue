<template>
  <div id="app">
    <!-- Шапка -->
    <header>
      <h1>Glossary Dashboard</h1>
      <nav>
        <router-link to="/">Главная</router-link>
        <button @click="logout" v-if="isAuthenticated">Выйти</button>
      </nav>
    </header>

    <!-- Контент -->
    <main>
      <router-view />
    </main>

    <!-- Подвал -->
    <footer>
      <p>© 2024 Glossary Service. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();

    const logout = () => {
      localStorage.removeItem("token"); // Удаляем токен
      router.push("/login"); // Перенаправляем на страницу входа
    };

    const isAuthenticated = !!localStorage.getItem("token");

    return {
      logout,
      isAuthenticated,
    };
  },
};
</script>

<style>
/* Базовые стили приложения */
#app {
  font-family: Arial, sans-serif;
  color: #333;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #007acc;
  margin-bottom: 20px;
  padding-bottom: 10px;
}

header h1 {
  margin: 0;
  font-size: 24px;
}

nav a {
  margin-right: 15px;
  color: #007acc;
  text-decoration: none;
  font-weight: bold;
}

nav a.router-link-active {
  text-decoration: underline;
}

main {
  min-height: 60vh;
}

footer {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #555;
}
</style>
