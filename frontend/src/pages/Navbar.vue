<template>
  <div>
    <nav class="bg-gray-900 border-b border-gray-200 px-4 py-3">
      <div class="max-w-screen-xl mx-auto flex items-center justify-between">
        <!-- Left (empty spacer) -->
        <div class="w-1/3"></div>

        <!-- Center (title/text) -->
        <div class="w-1/3 text-center">
          <span class="text-xl font-semibold text-white">GSO Inventory</span>
        </div>

        <!-- Right (buttons) -->
        <div class="w-1/3 flex justify-end space-x-2">
          <button
            class="text-white bg-blue-600 hover:bg-blue-700 font-medium rounded-lg text-sm px-4 py-2"
          >
            Add Equipment
          </button>

          <button
            @click="logout"
            class="text-white bg-red-600 hover:bg-red-700 font-medium rounded-lg text-sm px-4 py-2"
          >
            logout
          </button>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  router.push("/login");
};
</script>
