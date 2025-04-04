<template>
  <div>
    <Navbar />
    <Table :equipments="equipments" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import Navbar from "./Navbar.vue";
import Table from "../components/Table.vue";
import api from "../api/axios";

const router = useRouter();

//variables
const equipments = ref([]);

//fetch equipments
const fetchEquipments = async () => {
  try {
    const response = await api.get("equipments");
    equipments.value = response.data;
  } catch (error) {
    console.log("error in fetching all equipments: ", error);
  }
};

onMounted(fetchEquipments);
</script>
