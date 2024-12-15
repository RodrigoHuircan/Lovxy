const cards = document.getElementById('cards')
const items = document.getElementById('items')
const footer = document.getElementById('footer')
const templateCard = document.getElementById('template-card').content
const fragment = document.createDocumentFragment()
const templateFooter = document.getElementById('template-footer').content
const templateCarrito = document.getElementById('template-carrito').content
let carrito = {}

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
    if(localStorage.getItem('carrito')){
        carrito = JSON.parse(localStorage.getItem('carrito'))
        pintarCarrito()
    }
})

cards.addEventListener('click', e => {
    addCarrito(e)
})

items.addEventListener('click', e => {
    btnAccion(e)
})

const fetchData = () => {
    try {
        //const res = await fetch('api.json')
        //const data = await res.json()
        //console.log(data)
        const data = [
            {
              "precio": 50000,
              "id": 1,
              "title": "Collar",
              "thumbnailUrl": "https://picsum.photos/id/169/600"
            },
            {
              "precio": 30000,
              "id": 2,
              "title": "Correa Para Perros",
              "thumbnailUrl": "https://picsum.photos/id/237/600"
            },
            {
              "precio": 10000,
              "id": 3,
              "title": "Correa Para Gatos",
              "thumbnailUrl": "https://picsum.photos/id/219/600"
            },
            {
              "precio": 5000,
              "id": 4,
              "title": "Huesitos",
              "thumbnailUrl": "https://picsum.photos/id/582/600"
            },
            {
              "precio": 1000,
              "id": 5,
              "title": "Churu",
              "thumbnailUrl": "https://picsum.photos/id/40/600"
            },
            {
              "precio": 15000,
              "id": 6,
              "title": "Alimento Premium Para Perros",
              "thumbnailUrl": "https://picsum.photos/id/659/600"
            }
          ]
        pintarCards(data)
    } catch (error) {
        console.log(error)
    }
}

const pintarCards = data => {
    data.forEach(producto => {
        templateCard.querySelector('h5').textContent = producto.title
        templateCard.querySelector('p').textContent = producto.precio
        templateCard.querySelector('img').setAttribute("src", producto.thumbnailUrl)
        templateCard.querySelector('.btn-outline-dark').dataset.id = producto.id
        const clone = templateCard.cloneNode(true)
        fragment.appendChild(clone)
    })
    cards.appendChild(fragment)
}


const addCarrito = e => {
    //console.log(e.target)
    //console.log(e.target.classList.contains('btn-outline-dark'))
    if (e.target.classList.contains('btn-outline-dark')) {
        setCarrito(e.target.parentElement) 
    }
    e.stopPropagation()
}

const setCarrito = objeto => {
    console.log(objeto)
    const producto = {
        id: objeto.querySelector('.btn-outline-dark').dataset.id,
        tittle: objeto.querySelector('h5').textContent,
        precio: objeto.querySelector('p').textContent,
        cantidad: 1
    }

    if(carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1
    }

    carrito[producto.id] = {...producto}
    pintarCarrito()
}

const pintarCarrito = () => {
    console.log(carrito)
    items.innerHTML = ''
    Object.values(carrito).forEach(producto => {
        templateCarrito.querySelector('th').textContent = producto.id
        templateCarrito.querySelectorAll('td')[0].textContent = producto.tittle
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad
        templateCarrito.querySelector('.btn-info').dataset.id = producto.id
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.id
        templateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio

        const clone = templateCarrito.cloneNode(true)
        fragment.appendChild(clone)
    })
    items.appendChild(fragment)

    pintarFooter()

    localStorage.setItem('carrito', JSON.stringify(carrito))
}

const pintarFooter = () => {
    footer.innerHTML = ''
    if(Object.keys(carrito).length === 0){
        footer.innerHTML = '<th scope="row" colspan="5">Carrito vacío - comience a comprar!</th>'

        return
    }

    const nCantidad = Object.values(carrito).reduce((acc, {cantidad}) => acc + cantidad, 0)
    const nPrecio = Object.values(carrito).reduce((acc, {cantidad,precio}) => acc + (cantidad * precio),0)

    templateFooter.querySelectorAll('td')[0].textContent = nCantidad
    templateFooter.querySelector('span').textContent = nPrecio

    const clone = templateFooter.cloneNode(true)
    fragment.appendChild(clone)
    footer.appendChild(fragment)

    const btnVaciar = document.getElementById('vaciar-carrito')
    btnVaciar.addEventListener('click', () => {
        carrito = {};
        pintarCarrito()
    })
}

const btnAccion = e => {
    console.log(e.target)
    //Acción de aumentar
    if(e.target.classList.contains('btn-info')) {
        carrito[e.target.dataset.id]

        const producto = carrito[e.target.dataset.id]
        producto.cantidad = carrito[e.target.dataset.id].cantidad + 1
        carrito[e.target.dataset.id] = {...producto}
        pintarCarrito()
    }

    if(e.target.classList.contains('btn-danger')) {
        carrito[e.target.dataset.id]

        const producto = carrito[e.target.dataset.id]
        producto.cantidad = carrito[e.target.dataset.id].cantidad - 1
        if (producto.cantidad === 0) {
            delete carrito[e.target.dataset.id]
        }
        pintarCarrito()
    }

    e.stopPropagation()
}

