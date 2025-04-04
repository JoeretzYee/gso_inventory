<!-- components/EditEquipmentModal.vue -->
<template>
  <div
    ref="modalElement"
    id="editEquipmentModal"
    tabindex="-1"
    aria-hidden="true"
    class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
  >
    <div class="relative p-4 w-full max-w-2xl max-h-full">
      <div
        class="relative bg-gray-800 rounded-lg shadow border border-gray-700"
      >
        <!-- Modal header -->
        <div
          class="flex items-center justify-between p-4 border-b border-gray-700"
        >
          <h3 class="text-xl font-semibold text-white">Edit Equipment</h3>
        </div>

        <!-- Modal body -->
        <div class="p-4 space-y-4">
          <form @submit.prevent="handleSubmit">
            <div class="grid gap-4 mb-4 grid-cols-2">
              <!-- Inside EditEquipmentModal.vue's form -->

              <div class="col-span-2">
                <label
                  for="article"
                  class="block mb-2 text-sm font-medium text-white"
                  >Article</label
                >
                <input
                  type="text"
                  id="article"
                  v-model="formData.article"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="description"
                  class="block mb-2 text-sm font-medium text-white"
                  >Description</label
                >
                <input
                  type="text"
                  id="description"
                  v-model="formData.description"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="property_number"
                  class="block mb-2 text-sm font-medium text-white"
                  >Property Number</label
                >
                <input
                  type="text"
                  id="property_number"
                  v-model="formData.property_number"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="cost"
                  class="block mb-2 text-sm font-medium text-white"
                  >Cost</label
                >
                <input
                  type="number"
                  id="cost"
                  v-model="formData.cost"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="location"
                  class="block mb-2 text-sm font-medium text-white"
                  >Location</label
                >
                <select
                  id="location"
                  v-model="formData.location"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                >
                  <option value="mo">MO</option>
                  <option value="sef">SEF</option>
                  <option value="mdrrmo">MDRRMO</option>
                </select>
              </div>
              <div>
                <label
                  for="condition"
                  class="block mb-2 text-sm font-medium text-white"
                  >Condition</label
                >
                <select
                  id="condition"
                  v-model="formData.condition"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                >
                  <option value="Serviceable">Serviceable</option>
                  <option value="Unserviceable">Unserviceable</option>
                </select>
              </div>
              <div class="col-span-2">
                <label
                  for="remarks"
                  class="block mb-2 text-sm font-medium text-white"
                  >Remarks</label
                >
                <textarea
                  id="remarks"
                  v-model="formData.remarks"
                  class="border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
                ></textarea>
              </div>
            </div>
            <div class="flex justify-end pt-4 border-t border-gray-700">
              <!-- <button
                type="button"
                @click="closeModal"
                class="text-white bg-gray-600 hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-500 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
              >
                Cancel
              </button> -->
              <button
                type="submit"
                :disabled="isLoading"
                class="ms-3 text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center disabled:opacity-50"
              >
                {{ isLoading ? "Saving..." : "Save Changes" }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted, defineExpose } from "vue";
import { Modal } from "flowbite";
import api from "../api/axios";
import { showErrorAlert, showSuccessAlert } from "../lib/SwalAlerts";

const props = defineProps({
  equipment: {
    type: Object,
    required: true,
  },
});

const modalElement = ref(null);
let modal = null;

onMounted(() => {
  modal = new Modal(modalElement.value);
});

onUnmounted(() => {
  modal?.dispose(); // Cleanup to prevent memory leaks
});

defineExpose({
  showModal: () => modal?.show(),
});

const emit = defineEmits(["close", "saved"]);

const isLoading = ref(false);
const formData = ref({ ...props.equipment });
// const formData = ref({
//   ...props.equipment,
//   classification: props.equipment.classification_details,
// });

console.log(props.equipment);

watch(
  () => props.equipment,
  (newVal) => {
    formData.value = { ...newVal };
  }
);

const handleSubmit = async () => {
  try {
    isLoading.value = true;
    console.log("Submitting payload:", formData.value);
    const payload = {
      article: formData.value.article,
      description: formData.value.description,
      property_number: formData.value.property_number,
      cost: parseFloat(formData.value.cost), // Ensure number format
      location: formData.value.location.toLowerCase(), // Match API format
      condition: formData.value.condition,
      remarks: formData.value.remarks,
      classification: formData.value.classification_details.id,
      //   classification: formData.value.classification_details.id,
    };

    const response = await api.put(`equipments/${formData.value.id}/`, payload);
    showSuccessAlert("Success", "Equipment updated successfully!");
    // window.location.reload();
    setTimeout(() => {
      window.location.reload();
    }, 1500);
  } catch (error) {
    console.error("Error updating equipment:", error);

    showErrorAlert("Update Field", "Error in Updating the equipment");
  }
};

const closeModal = () => {
  const modalElement = document.getElementById("editEquipmentModal");
  const modal = Modal.getInstance(modalElement) || new Modal(modalElement);
  modal.hide();
  emit("close");
};
</script>
