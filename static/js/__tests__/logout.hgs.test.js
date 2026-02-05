/**
 * @jest-environment jsdom
 */

const { attachConfirmToForm } = require("../logout.hgs");

test("prevents logout form submit when user cancels", () => {
  document.body.innerHTML = `
    <form method="post" action="/logout/">
      <button type="submit" class="js-confirm-logout">Logout</button>
    </form>
  `;

  window.confirm = jest.fn(() => false);

  const form = document.querySelector("form");
  attachConfirmToForm(form, "Log out now?");

  const event = new Event("submit", { bubbles: true, cancelable: true });
  form.dispatchEvent(event);

  expect(window.confirm).toHaveBeenCalledWith("Log out now?");
  expect(event.defaultPrevented).toBe(true);
});

test("allows logout form submit when user confirms", () => {
  document.body.innerHTML = `
    <form method="post" action="/logout/">
      <button type="submit" class="js-confirm-logout">Logout</button>
    </form>
  `;

  window.confirm = jest.fn(() => true);

  const form = document.querySelector("form");
  attachConfirmToForm(form, "Log out now?");

  const event = new Event("submit", { bubbles: true, cancelable: true });
  form.dispatchEvent(event);

  expect(event.defaultPrevented).toBe(false);
});
