// const openBtn = document.querySelector("#open-btn")
// const closeBtn = document.querySelector(".close-btn")
// const offcanvasMenu = document.querySelector(".offcanvas-menu")

// openBtn.addEventListener("click", function (e) {
//   e.preventDefault()
//   offcanvasMenu.classList.add("active")
// })

// closeBtn.addEventListener("click", function (e) {
//   e.preventDefault()
//   offcanvasMenu.classList.remove("active")
// })

// // -------> delet product form the list
// const deleteButtons = document.querySelectorAll(".delete_btn")

// deleteButtons.forEach((button) => {
//   button.addEventListener("click", () => {
//     const card = button.closest(".card")
//     if (card) {
//       card.remove()
//     }
//   })
// })


// document.getElementById("menu_content").addEventListener("click", function (event) {
//   if (event.target.classList.contains("delete_btn")) {
//     var card = event.target.closest(".card")
//     card.parentNode.removeChild(card)
//   }
// })





// async function del_from_the_comparator(id){

//   const url ="{%url "get comparer data"%}";
//   const data = {
//     item_id: id,
//     delete: true,
//   };
  
//   fetch(url, {
//     method: 'GET',
//   })
//   .then(response => {
//     for(item of response){
//       alert(item);  


//     }
//     alert('yser');  
//   })
//   .catch(error => {
//     // Handle error
//   });
// }









// async function del_from_comparator(id){

//   const url ="{{request.get_full_uri}}";
//   const data = {
//     item_id: id,
//     delete: true,
//   };
  
//   fetch(url, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json' // Specify content type
//     },
//     body: JSON.stringify(data)
//   })
//   .then(response => {

//     alert('yser');  
//   })
//   .catch(error => {
//     // Handle error
//   });
// }








const openBtn = document.querySelector("#open-btn")
const closeBtn = document.querySelector(".close-btn")
const offcanvasMenu = document.querySelector(".offcanvas-menu")

openBtn.addEventListener("click", function (e) {
  e.preventDefault()
  offcanvasMenu.classList.add("active")
})

closeBtn.addEventListener("click", function (e) {
  e.preventDefault()
  offcanvasMenu.classList.remove("active")
})

// -------> delet product form the list
const deleteButtons = document.querySelectorAll(".delete_btn")

deleteButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const card = button.closest(".compare_card")
    if (card) {
      card.remove()
    }

  })
})



async function delCompaItem(id){
  console.log('starting');
  const url = `http://127.0.0.1:8000/compar/del/${id}`
  const response = await fetch(url ,{
      method:'GET',
      headers: {
          'Content-Type': 'application/json',
          'comparer_item_id':id,
      },
  });

  if (response.ok) {
      const jsonResponse = await response.json();
      console.log('Success:', jsonResponse);
      // alert('deleted');
  } else {
      console.error('Error:', response.statusText);
  }
};