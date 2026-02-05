/**
 * Turn text into a URL-friendly slug.
 * Examples:
 *  "Field Maple" -> "field-maple"
 *  "  Apple   Tree " -> "apple-tree"
 */

function slugify(text) {
  return String(text)
    .trim()
    .toLowerCase()
    .replace(/['"]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

/**
 * Attach a confirm() prompt to any element matching selector.
 * If user cancels, prevent default (useful for delete links/forms).
 */
function attachConfirm(selector, message = "Are you sure?") {
  const elements = document.querySelectorAll(selector);
  elements.forEach((el) => {
    el.addEventListener("click", (e) => {
      const ok = window.confirm(message);
      if (!ok) e.preventDefault();
    });
  });
}

module.exports = { slugify, attachConfirm };
