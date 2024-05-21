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


// ---------------------------------------------------------------------

async function delete_category(id){
  console.log('wrking');
  let cat_del_url=`http://localhost:8000/dashboard/category/del/${id}`;

  fetch(cat_del_url, {
    method: 'GET'  // Replace with 'POST', 'PUT', or 'DELETE' if needed
  })
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Handle the fetched data (e.g., display, update UI)
    console.log(data);
    alert(data['message']);
 

  })
  .catch(error => {
    // Handle errors (e.g., display error message)
    console.error('Error fetching data:', error);
  });


}

