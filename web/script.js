const kind = document.getElementById("kind");
const entry = document.getElementById("entry");
const result = document.getElementById("result");
const reason = document.getElementById("reason");
const model = document.getElementById("model");

function validatePassword(s) {
  const special = "!@#$%^&*()-_+=";
  if (s.length < 8 || s.length > 16) return [false, "Length must be 8–16 characters."];
  if (/\s/.test(s)) return [false, "Spaces are not allowed."];
  if (!/[A-Z]/.test(s)) return [false, "Add an uppercase letter."];
  if (!/[a-z]/.test(s)) return [false, "Add a lowercase letter."];
  if (!/[0-9]/.test(s)) return [false, "Add a digit."];
  if (![...s].some(c => special.includes(c))) return [false, "Add an allowed special character."];
  if ([...s].some(c => !/[A-Za-z0-9]/.test(c) && !special.includes(c))) return [false, "Unsupported character."];
  return [true, "Password satisfies the defined rules."];
}
function validateEmail(s) {
  const localAtom = "[A-Za-z0-9_%+-]+";
  const pattern = new RegExp("^" + localAtom + "(?:\\." + localAtom + ")*@" +
    "[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)*\\.[A-Za-z]{2,}$");
  if (/\s/.test(s)) return [false, "Spaces are not allowed."];
  if (s.length > 254 || !pattern.test(s)) return [false, "Email does not match the defined format."];
  const [local, domain] = s.split("@");
  if (local.length > 64 || domain.split(".").some(label => label.length > 63))
    return [false, "Local part or domain label is too long."];
  return [true, "Email follows the defined format."];
}
function validatePin(s) {
  return /^[0-9]{4}$/.test(s) ? [true, "Valid four-digit PIN."] :
    [false, "PIN must contain exactly four digits (0–9)."];
}
function updateModel() {
  const descriptions = {
    password: "DFA summary: length counter 0–16 + four flags (uppercase, lowercase, digit, special). Unsupported characters or length above 16 enter the dead state. Accept when length is 8–16 and every flag is set.",
    email: "Finite-state scan: local-part characters and dot placement → exactly one @ → domain labels → final extension of at least two letters. This is a defined subset of email syntax.",
    pin: "DFA states q0 → q1 → q2 → q3 → q4. Each digit advances one state; q4 is accepting. A non-digit or fifth digit enters a dead state."
  };
  model.textContent = descriptions[kind.value];
}
document.getElementById("check").addEventListener("click", () => {
  const functions = { password: validatePassword, email: validateEmail, pin: validatePin };
  const [ok, message] = functions[kind.value](entry.value);
  result.textContent = ok ? "ACCEPTED" : "REJECTED";
  result.className = ok ? "accept" : "reject";
  reason.textContent = message;
});
kind.addEventListener("change", updateModel);
updateModel();
