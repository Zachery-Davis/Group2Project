const form = document.querySelector("form");
const regInput = document.querySelector("#regInput");
const confirmPassword = regInput.querySelector("input");
const f1Button = document.querySelector(".F1-button");
const f2Button = document.querySelector(".F2-button");

f2Button.addEventListener("click", (event) => {
  const isLogin = f1Button.innerText === "Login";

  // Toggle between login and register states
  regInput.style.display = isLogin ? "block" : "none";
  confirmPassword.required = isLogin;
  f1Button.innerText = isLogin ? "Register" : "Login";
  f2Button.innerText = isLogin ? "Login" : "Don't have an account? Register";
  document.querySelector("h2").innerText = isLogin ? "Register" : "Login";
});

document.querySelector("form").addEventListener("submit", function (event) {
  // Get the current form action
  const formAction = document.querySelector("form").getAttribute("action");

  // If the form is set to "register", ensure both passwords match
  if (formAction === "register") {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("password2");

    if (password.value !== confirmPassword.value) {
      event.preventDefault(); // Stop form submission
      confirmPassword.setCustomValidity("Passwords do not match.");
    }
  }
});
