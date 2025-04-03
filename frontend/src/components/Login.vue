<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gray-100 dark:bg-gray-900"
  >
    <div class="relative w-full max-w-sm">
      <!-- Container for flip effect -->
      <div class="flip-container" :class="{ flipped: isSignup }">
        <!-- Front: Login Form -->
        <div class="flip-card front">
          <div
            class="p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
          >
            <form @submit.prevent="login" class="space-y-6">
              <h5
                class="text-xl text-center font-medium text-gray-900 dark:text-white"
              >
                Login
              </h5>
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Email</label
                >
                <input
                  type="email"
                  id="email"
                  class="input-field"
                  placeholder="name@gmail.com"
                  v-model="loginEmail"
                  required
                />
              </div>
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <input
                  type="password"
                  id="password"
                  placeholder="••••••••"
                  class="input-field"
                  v-model="loginPassword"
                  required
                />
              </div>
              <button type="submit" class="submit-button">Submit</button>
              <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                Not registered?
                <button
                  @click.prevent="toggleForm"
                  class="text-blue-700 hover:underline dark:text-blue-500"
                >
                  Create account
                </button>
              </div>
            </form>
          </div>
        </div>

        <!-- Back: Sign Up Form -->
        <div class="flip-card back">
          <div
            class="p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
          >
            <form @submit.prevent="signup" class="space-y-6">
              <h5
                class="text-xl text-center font-medium text-gray-900 dark:text-white"
              >
                Sign Up
              </h5>
              <div>
                <label
                  for="name"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Email</label
                >
                <input
                  type="text"
                  id="name"
                  class="input-field"
                  placeholder="name@gmail.com"
                  v-model="signupEmail"
                  required
                />
              </div>
              <div>
                <label
                  for="password-signup"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <input
                  type="password"
                  id="password-signup"
                  placeholder="••••••••"
                  class="input-field"
                  v-model="signupPassword"
                  required
                />
              </div>
              <button type="submit" class="submit-button">Submit</button>
              <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                Already have an account?
                <button
                  @click.prevent="toggleForm"
                  class="text-blue-700 hover:underline dark:text-blue-500"
                >
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { showSuccessAlert, showErrorAlert } from "../lib/SwalAlerts.js";
import api from "../api/axios.js";

const router = useRouter();

const isSignup = ref(false);
const signupEmail = ref("");
const signupPassword = ref("");
const loginEmail = ref("");
const loginPassword = ref("");

const toggleForm = () => {
  isSignup.value = !isSignup.value;
};

// Sign Up Function
const signup = async () => {
  try {
    const response = await api.post("users/", {
      email: signupEmail.value,
      password: signupPassword.value,
    });

    showSuccessAlert(
      "Account Created",
      "Your account has been created successfully!"
    );
    isSignup.value = false;
  } catch (error) {
    let errorMessage =
      error.response?.data?.error || "Email or Password Already Exist";
    showErrorAlert("Signup Failed", errorMessage);
  }
};

//login function
const login = async () => {
  try {
    const response = await api.post("token/", {
      email: loginEmail.value,
      password: loginPassword.value,
      username: loginEmail.value,
    });

    if (response.status == 200) {
      showSuccessAlert("Login Successful", "Redirecting now in Homepage");
      localStorage.setItem("accessToken", response.data.access);
      localStorage.setItem("refreshToken", response.data.refresh);
      router.push("/");
    }
  } catch (error) {
    let errorMessage = error.response?.data?.error || "Wrong Credentials";
    showErrorAlert("Wrong Credentials", errorMessage);
  }
};
</script>

<style scoped>
/* Flip Container */
.flip-container {
  perspective: 1000px;
  position: relative;
  width: 100%;
  height: 400px; /* Adjust height as needed */
}

/* Flip Card */
.flip-card {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  transition: transform 0.6s ease-in-out;
}

/* Front Side */
.front {
  transform: rotateY(0deg);
}

/* Back Side */
.back {
  transform: rotateY(180deg);
}

/* When flipped, rotate both sides */
.flipped .front {
  transform: rotateY(-180deg);
}

.flipped .back {
  transform: rotateY(0deg);
}

/* Input Fields */
.input-field {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  transition: border 0.3s ease;
}

.input-field:focus {
  border-color: #2563eb;
  outline: none;
}

/* Submit Button */
.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.submit-button:hover {
  background-color: #1e40af;
}
</style>
