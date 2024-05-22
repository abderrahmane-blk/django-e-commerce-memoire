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

// 

// ! show form
let edit_btns = document.querySelectorAll(".editBtn")
let form_body = document.querySelector(".form_container")
let add_btn = document.querySelector(".add_btn")
let form =document.getElementById('editForm')

function showForm(cat_id) {
  form_body.classList.add("form_visible");
  let the_url =`http://127.0.0.1:8000/dashboard/category/edit/${cat_id}/  `
  form.setAttribute("action", the_url);

}

function hiddeForm() {
  form_body.classList.remove("form_visible");
  form.removeAttribute("action");

}


//! for products

let edit_btns2 = document.querySelectorAll(".editBtn2")
let form_body2 = document.querySelector("#form_container2")
let add_btn2 = document.querySelector(".add_btn2")
let form2 =document.getElementById('editForm2')
let the_form =document.getElementById('editForm2')

function showForm2(p_id) {
  form_body2.classList.add("form_visible");
  console.log("show form2 called");
  // let a = {% url "edit product" %};
  let the_url =`http://127.0.0.1:8000/dashboard/product/edit/${p_id}/  `
  the_form.setAttribute("action", the_url);

}

function hiddeForm2() {
  form_body2.classList.remove("form_visible");
  the_form.removeAttribute("action");

}

function showForm3() {
  form_body2.classList.add("form_visible");
  console.log("product add form called");
  // let a = {% url "edit product" %};
  let the_url =`http://127.0.0.1:8000/dashboard/products/add/  `
  the_form.setAttribute("action", the_url);

}




// del product

async function delete_product(id){
  console.log('wrking');
  let cat_del_url=`http://localhost:8000/dashboard/product/del/${id}`;

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


