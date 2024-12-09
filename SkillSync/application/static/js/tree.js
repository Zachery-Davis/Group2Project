// TreePage
if (document.querySelector(".tree")) {
  // Close dropdown if clicked outside
  window.addEventListener("click", (event) => {
    if (!event.target.matches("button") && !event.target.matches("i")) {
      document.querySelectorAll(".show")?.forEach((element) => {
        element.classList.remove("show");
      });
      document.querySelector("button.selected")?.classList.remove("selected");
      currentNode = null;
    }
  });

  let currentNode = null;
  document.querySelectorAll(".tree button").forEach((button) => {
    button.addEventListener("click", (event) => {
      const infoPanel = document.querySelector(".info-panel");
      const infoTitle = document.getElementById("infoTitle");
      const infoDescription = document.getElementById("infoDescription");

      const title = button.textContent;
      const nodeElement = event.target;
      let description = "";

      findDescription(jsonData);
      function findDescription(value) {
        if (value.title == title) {
          description = value.description;
          return;
        }

        if (value.extend && Object.keys(value.extend).length > 0) {
          for (let key in value.extend) {
            findDescription(value.extend[key]); // Recurse into nested objects
          }
        }
      }

      if (currentNode === nodeElement) {
        infoPanel.classList.remove("show");
        nodeElement.classList.remove("selected"); // Remove selection from the node
        currentNode = null;
      } else {
        if (currentNode) {
          // Remove 'selected' class from previously selected node
          document.querySelector("button.selected")?.classList.remove("selected");
        }

        infoTitle.textContent = title;
        infoDescription.textContent = description;
        infoPanel.classList.add("show");
        nodeElement.classList.add("selected"); // Add selection to the clicked node
        currentNode = nodeElement;
      }
    });
  });

  // Initialize scale and translation
  let scale = 1;
  let translateX = 0;
  let translateY = 0;

  const tree = document.querySelector(".tree");
  const zoomBtn = document.querySelector(".fa-expand");

  window.addEventListener("wheel", (event) => {
    // Adjust the zoom scale
    const zoomFactor = event.deltaY * -0.001;
    const oldScale = scale;
    scale = Math.min(Math.max(0.75, scale + zoomFactor), 2.5);

    // Calculate the scaling adjustment
    const scaleAdjustment = 1 - scale / oldScale;

    translateX += (event.clientX - translateX) * scaleAdjustment;
    translateY += (event.clientY - translateY) * scaleAdjustment;

    // Apply the transform with new scale and translation
    tree.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;

    // Show the reset zoom button
    zoomBtn.style.display = "block";
  });

  // Drag
  dragElement(document.querySelector(".tree-container"));

  function dragElement(container) {
    // Get the inner ul element within tree-container to move it on drag
    const elmnt = container.querySelector("ul");

    let startX = 0,
      startY = 0,
      initialX = 0,
      initialY = 0;

    container.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
      e = e || window.event;
      e.preventDefault();

      container.style.cursor = "grabbing";
      zoomBtn.style.display = "block";

      // Record the initial cursor position and element position
      startX = e.clientX;
      startY = e.clientY;
      initialX = elmnt.offsetLeft;
      initialY = elmnt.offsetTop;

      document.onmouseup = closeDragElement;
      document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
      e = e || window.event;
      e.preventDefault();

      // Calculate the new cursor position
      let deltaX = e.clientX - startX;
      let deltaY = e.clientY - startY;

      // Set the inner ul element's new position based on initial position and deltas
      elmnt.style.position = "absolute"; // Ensure positioning is set
      elmnt.style.left = initialX + deltaX + "px";
      elmnt.style.top = initialY + deltaY + "px";
    }

    function closeDragElement() {
      document.onmouseup = null;
      document.onmousemove = null;

      container.style.cursor = "grab";
    }
  }

  function showTab(tabName) {
    // Hide all tab content
    document.querySelectorAll(".tab-content").forEach((tab) => (tab.style.display = "none"));
    // Remove active class from all tabs
    document.querySelectorAll(".tab").forEach((tab) => tab.classList.remove("active"));

    // Show the selected tab content and add active class to the corresponding tab button
    document.getElementById(`${tabName}Tab`).style.display = "block";
    document.querySelector(`.tab[onclick="showTab('${tabName}')"]`).classList.add("active");
  }

  // Set default tab to show on load
  showTab("description");
}
