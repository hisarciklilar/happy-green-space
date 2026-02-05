const { slugify } = require("../utils.slugify");

test("slugify lowercases and hyphenates words", () => {
  expect(slugify("Field Maple")).toBe("field-maple");
});

test("slugify trims and collapses extra spaces", () => {
  expect(slugify("  Apple   Tree ")).toBe("apple-tree");
});

test("slugify removes punctuation", () => {
  expect(slugify(`Jenny Porter (Erica)`)).toBe("jenny-porter-erica");
});
