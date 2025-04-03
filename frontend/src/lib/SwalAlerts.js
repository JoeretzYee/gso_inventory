import Swal from "sweetalert2";

export const showSuccessAlert = (title, text) => {
  Swal.fire({
    title: title || "Success!",
    text: text || "Operation completed successfully!",
    icon: "success",
    confirmButtonText: "OK",
  });
};

export const showErrorAlert = (title, text) => {
  Swal.fire({
    title: title || "Error!",
    text: text || "Something went wrong!",
    icon: "error",
    confirmButtonText: "OK",
  });
};
