const sidebar = document.querySelector(".sidebar");

sidebar.addEventListener("click", (event) => {
  if (event.target.classList.contains("tablinks")) {
    const tabName = event.target.innerText;

    document.querySelector(".tablinks.selected").classList.remove("selected");
    document.querySelector(".tabcontent.show").classList.remove("show");

    document.getElementById(tabName).classList.add("show");
    event.target.classList.add("selected");
  }
});
