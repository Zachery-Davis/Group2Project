// Dropdown Toggle
function toggleDropdown() {
  document.getElementById("dropdownMenu").classList.toggle("show");
}

// Close dropdown if clicked outside
window.addEventListener("click", (event) => {
  if (!event.target.closest(".dropdown-content") && !event.target.matches("i")) {
    document.getElementById("dropdownMenu").classList.remove("show");
  }
});
