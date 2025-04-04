<template>
  <div class="bg-gray-900 text-white p-4 rounded-lg shadow-md">
    <!-- Table Caption & Search Bar -->
    <div class="flex justify-between items-center pb-4">
      <h2 class="text-lg font-semibold">Equipment List</h2>

      <!-- Search and Button Container -->
      <div class="flex space-x-2 w-full max-w-md">
        <!-- Search Input -->
        <input
          id="searchInput"
          type="text"
          v-model="searchQuery"
          placeholder="Filter"
          class="bg-gray-800 text-white border border-gray-700 rounded-lg px-4 py-2 w-full focus:ring focus:ring-blue-500"
        />
        <!-- Button -->
        <button
          class="text-white bg-green-600 hover:bg-green-700 font-medium rounded-lg text-sm px-4 py-2"
        >
          Generate
        </button>
      </div>
    </div>
    <EditEquipmentModal
      v-if="selectedEquipment"
      :equipment="selectedEquipment"
      @close="selectedEquipment = null"
      ref="editModal"
    />

    <!-- Scrollable Table Container -->
    <div
      class="overflow-x-auto max-h-100 border border-gray-700 rounded-lg"
      style="height: calc(100vh - 22vh)"
    >
      <table class="min-w-full text-sm text-left text-gray-400">
        <thead class="bg-gray-800 text-gray-300 uppercase">
          <tr>
            <th class="px-6 py-3">Article</th>
            <th class="px-6 py-3">Description</th>
            <th class="px-6 py-3">Property Number</th>
            <th class="px-6 py-3">Cost</th>
            <th class="px-6 py-3">Location</th>
            <th class="px-6 py-3">Condition</th>
            <th class="px-6 py-3">Remarks</th>
            <th class="px-6 py-3">Actions</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <tr
            v-for="equipment in filterEquipments"
            :key="equipment.id"
            class="border-b border-gray-700"
          >
            <td class="px-6 py-4">{{ equipment.article }}</td>
            <td class="px-6 py-4">{{ equipment.description }}</td>
            <td class="px-6 py-4">{{ equipment.property_number }}</td>
            <td class="px-6 py-4">
              ₱{{ formatNumberWithCommas(equipment.cost) }}
            </td>
            <td class="px-6 py-4">{{ equipment.location }}</td>
            <!-- <td class="px-6 py-4">{{ equipment.condition }}</td> -->
            <td
              :class="{
                ' text-green-800 px-6 py-4':
                  equipment.condition === 'Serviceable',
                ' text-red-800 px-6 py-4':
                  equipment.condition === 'Unserviceable',
              }"
            >
              {{ equipment.condition }}
            </td>
            <td class="px-6 py-4">
              {{ equipment.remarks }}
            </td>
            <td class="px-6 py-4">
              <button
                type="button"
                @click="openEditModal(equipment)"
                class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-900"
              >
                Edit
              </button>

              &nbsp;
              <button
                @click="confirmDelete(equipment)"
                type="button"
                class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900"
              >
                Delete
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M3 6h18M9 6v12m6-12v12m-3 0h6m-6 0H9m-6 0H3m6 0h6"
                  />
                </svg>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from "vue";
import { formatNumberWithCommas } from "../utils/FormatNumberWithCommas";
import EditEquipmentModal from "../modals/EditEquipmentModal.vue";
import { showErrorAlert, showSuccessAlert } from "../lib/SwalAlerts";
import Swal from "sweetalert2";

const props = defineProps({
  equipments: Array,
});

const searchQuery = ref("");
const selectedEquipment = ref(null);
const editModal = ref(null);

const openEditModal = (equipment) => {
  selectedEquipment.value = { ...equipment };
  nextTick(() => {
    if (editModal.value) {
      editModal.value.showModal(); // Use the exposed method
    }
  });
};

const deleteEquipment = async (equipmentId) => {
  try {
    console.log("Deleting equipment with ID:", equipmentId);
    const response = await api.delete(`equipments/${equipmentId}/`);
    showSuccessAlert("Success", "Delete Successful");
  } catch (error) {
    showErrorAlert("Error", "Error in deleting the equipment");
  }
};

const confirmDelete = (equipment) => {
  Swal.fire({
    title: "Are you sure?",
    text: `You are about to delete equipment: ${equipment.article}`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes, delete it!",
    cancelButtonText: "No, keep it",
    reverseButtons: true,
  }).then((result) => {
    if (result.isConfirmed) {
      // Proceed with the deletion
      deleteEquipment(equipment.id);
    }
  });
};

const filterEquipments = computed(() => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return props.equipments;

  const filters = {};
  let hasKeyValuePairs = false;

  // Parse key:value pairs
  query.split(/\s+/).forEach((part) => {
    const [key, ...values] = part.split(/[:=]/);
    if (key && values.length) {
      hasKeyValuePairs = true;
      const value = values.join(":").trim().toLowerCase();
      filters[key.trim().toLowerCase()] = value;
    }
  });

  return props.equipments.filter((equipment) => {
    if (hasKeyValuePairs) {
      return Object.entries(filters).every(([key, value]) => {
        const equipmentValue = String(equipment[key] || "").toLowerCase();
        return key === "location" || key === "condition"
          ? equipmentValue === value
          : equipmentValue.includes(value);
      });
    }

    // Free-text search with priority to exact matches
    return [
      equipment.location.toLowerCase() === query, // Exact location match
      equipment.condition.toLowerCase() === query, // Exact condition match
      equipment.article.toLowerCase().includes(query),
      equipment.property_number.toLowerCase().includes(query),
      equipment.remarks?.toLowerCase().includes(query),
    ].some(Boolean);
  });
});
</script>
