export function choosePlural(value, pluralForms) {
  const twoDigits = Math.abs(value) % 100;
  const lastDigit = value % 10;
  if (twoDigits > 10 && twoDigits < 20) return pluralForms[2];
  if (lastDigit > 1 && lastDigit < 5) return pluralForms[1];
  if (lastDigit === 1) return pluralForms[0];
  return pluralForms[2];
}
