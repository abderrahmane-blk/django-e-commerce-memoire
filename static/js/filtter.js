const btns = [
  {
    id: 1,
    name: "Mobiles"
  },
  {
    id: 2,
    name: "Watches"
  },
  {
    id: 3,
    name: "Cameras"
  },
  {
    id: 4,
    name: "Laptops"
  },
  {
    id: 5,
    name: "Air Pods"
  }
]

const filters = [
  ...new Set(
    btns.map((btn) => {
      return btn
    })
  )
]

document.getElementById("btns").innerHTML = filters
  .map((btn) => {
    var { name, id } = btn
    return "<button class='fil-p' onclick='filterItems(" + id + `)'>${name}</button>`
  })
  .join("")

const product = [
  {
    id: 1,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Z Flip Foldable Mobile",
    price: 120,
    category: "mobile"
  },
  {
    id: 5,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Air Pods Pro",
    price: 60,
    category: "airpods"
  },
  {
    id: 3,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "250D DSLR Camera",
    price: 230,
    category: "cameras"
  },
  {
    id: 1,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Foldable Mobile",
    price: 300
  },
  {
    id: 5,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Air Pods Pro",
    price: 65,
    category: "airpods"
  },
  {
    id: 3,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "DSLR Camera",
    price: 200,
    category: "cameras"
  },
  {
    id: 4,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Laptop",
    price: 100,
    category: "Laptop"
  },
  {
    id: 1,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Mobile",
    price: 350
  },
  {
    id: 3,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "DSLR Camera",
    price: 130,
    category: "cameras"
  },
  {
    id: 5,
    image: "assets/Screenshot 2023-12-02 010945.png",
    title: "Air Pods",
    price: 85,
    category: "airpods"
  }
]

const categories = [
  ...new Set(
    product.map((item) => {
      return item
    })
  )
]

const filterItems = (a) => {
  const flterCategories = categories.filter(item)
  function item(value) {
    if (value.id == a) {
      return value.id
    }
  }
  displayItem(flterCategories)
}

const displayItem = (items) => {
  document.getElementById("root").innerHTML = items
    .map((item) => {
      var { image, title, price } = item
      return `
          <div class="filter_product-card">
              <div class="filter_product-image">
                <span class="filter_discount-tag">50% off</span>
                <a href="productPage.html">
                  <img src="${image}" class="filter_product-thumb" alt="" />
                </a>
                <button class="filter_card-btn">add to Cart</button>
              </div>
              <div class="filter_product-info">
                <h2 class="filter_product-brand">${title}</h2>
                <span class="filter_price">${price}.00</span>
                <span class="filter_actual-price">$40</span>
              </div>
            </div>
      `
    })
    .join("")
}
displayItem(categories)

document.querySelectorAll(".fil-p").forEach((btn) => {
  btn.addEventListener("click", function (event) {
    event.preventDefault()
  })
})
