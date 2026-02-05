// Shared JavaScript helpers for Happy Green Space

document.addEventListener("DOMContentLoaded", () => {
  // Logout confirmation
  const logoutButton = document.querySelector(".js-confirm-logout");
  if (logoutButton && logoutButton.form) {
    attachConfirmToForm(logoutButton.form, "Log out now?");
  }
});

if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    attachConfirmToForm,
  };
}
