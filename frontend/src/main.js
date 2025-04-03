import { createApp } from "vue";
import App from "./App.vue";
import "./assets/main.css";
import "flowbite";
import router from "../src/router/index";

const app = createApp(App);
app.use(router);
app.mount("#app");
