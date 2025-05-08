function toggleMenu() {
  menuButton = document.getElementById("menu-cross")
  menuClose = document.getElementById("cross")
  dropdown = document.getElementById("menu")

  menuButton.classList.toggle("hidden")
  menuClose.classList.toggle("hidden")

  dropdown.classList.toggle("hidden")
}