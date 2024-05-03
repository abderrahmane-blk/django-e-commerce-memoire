// add hovered class to selected list item
let list = document.querySelectorAll(".nav")
function activeLink() {
  list.forEach((item) => {
    item.classList.remove("clicked")
  })
  this.classList.add("clicked")
}
list.forEach((item) => {
  item.addEventListener("mouseover", activeLink)
})

list.forEach((item) => {
  item.addEventListener("click", activeLink)
})

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
