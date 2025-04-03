import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Home from "../pages/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("accessToken") !== null;

  if (to.meta.requiresAuth && !isAuthenticated) {
    next("/login"); // Redirect to login if not authenticated
  } else {
    next();
  }
});

export default router;
