<template>
  <div>
    HOme

    <button @click="logout">logout</button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
console.log(localStorage.getItem("accessToken"));

const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  router.push("/login");
};
</script>

<style scoped></style>
