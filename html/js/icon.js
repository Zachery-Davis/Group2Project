//HEADER

// Dropdown Toggle
function toggleDropdown() {
  document.getElementById("dropdownMenu").classList.toggle("show");
}

// Close dropdown if clicked outside
if (document.querySelector(".fa-bars")) {
  window.addEventListener("click", (event) => {
    if (!event.target.closest(".dropdown-content") && !event.target.matches("i")) {
      document.getElementById("dropdownMenu").classList.remove("show");
    }
  });
}

//FOOTER

// Reset zoom function
function resetScale() {
  // Reset scale
  scale = 1;
  tree.style.transform = `scale(1)`;

  // Get container and tree dimensions as numbers
  let container = document.querySelector(".tree-container");
  let containerWidth = parseFloat(window.getComputedStyle(container).width);
  let containerHeight = parseFloat(window.getComputedStyle(container).height);
  let treeWidth = parseFloat(window.getComputedStyle(tree).width);
  let treeHeight = parseFloat(window.getComputedStyle(tree).height);

  // Calculate centered positions
  let centerX = (containerWidth - treeWidth) / 2;
  let centerY = (containerHeight - treeHeight) / 2;

  // Apply centering and reset position
  tree.style.left = `${centerX}px`;
  tree.style.top = `${centerY}px`;

  // Hide the zoom button
  zoomBtn.style.display = "none";
}

// Dark Mode Toggle
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}
