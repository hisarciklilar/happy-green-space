// Shared JavaScript helpers for Happy Green Space

function attachConfirmToForm(form, message) {
  form.addEventListener("submit", (e) => {
    if (!window.confirm(message)) {
      e.preventDefault();
      e.stopPropagation();
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  // Logout confirmation
  const logoutButton = document.querySelector(".js-confirm-logout");
  if (logoutButton && logoutButton.form) {
    attachConfirmToForm(logoutButton.form, "Log out now?");
  }
});

// For Jest / Node tests only
if (typeof module !== "undefined" && module.exports) {
  module.exports = { attachConfirmToForm };
}
