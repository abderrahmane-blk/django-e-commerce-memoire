// add hovered class to selected list item

let list = document.querySelectorAll(".nav")
function activeLink() {
  list.forEach((item) => {
    item.classList.remove("clicked")
  })
  this.classList.add("clicked")
}
list.forEach((item) => {
  item.addEventListener("click", activeLink)
})



// !--------------> sub menu <------------
let subMenu = document.getElementById("subMenu")
function togglMenu() {
  subMenu.classList.toggle("open-menu")
}
function handleClickOutside(event) {
  if (!subMenu.contains(event.target) && !event.target.matches("button")) {
    subMenu.classList.remove("open-menu")
  }
}

// Listen for clicks on the entire document
document.addEventListener("click", handleClickOutside)








// Menu Toggle
let toggle = document.querySelector(".toggle")
let navigation = document.querySelector(".slider")
let main = document.querySelector(".main")

toggle.onclick = function () {
  navigation.classList.toggle("active")
  main.classList.toggle("active")
}

const deletButtons = document.querySelectorAll(".delete_row")
const banButtons = document.querySelectorAll(".ban_btn")

banButtons.forEach((button) => {
  button.addEventListener("click", function (event) {
    if (event.target.innerText.toLowerCase() === "ban") {
      event.target.innerText = "Banned"
    } else {
      event.target.innerText = "Ban"
    }
  })
})

deletButtons.forEach((button) => {
  button.addEventListener("click", function (event) {
    const row = event.target.closest(".table_row")
    if (row) {
      row.remove()
    }
  })
})
