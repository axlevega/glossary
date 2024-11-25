import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../components/Dashboard.vue";
import ProjectDetails from "../components/ProjectDetails.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";

const routes = [
  { path: "/", name: "Dashboard", component: Dashboard },
  { path: "/project/:id", name: "ProjectDetails", component: ProjectDetails },
  { path: "/login", name: "Login", component: Login },
  { path: "/register", name: "Register", component: Register }, // Маршрут на страницу регистрации
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem("token");
  if (!isAuthenticated && to.name !== "Login" && to.name !== "Register") {
    next({ name: "Login" });
  } else {
    next();
  }
});

export default router;
