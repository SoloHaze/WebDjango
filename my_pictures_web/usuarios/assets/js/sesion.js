let usuarioLogeado =  JSON.parse(localStorage.getItem("sesion"))

let navbar = document.getElementById("navbar");





if(usuarioLogeado){

    if(usuarioLogeado.tipo =="admin"){
        let liPinturas =  document.createElement("li")
        liPinturas.innerHTML = `<a href="productosAdmin.html">Pinturas</a>`
    
        navbar.appendChild(liPinturas)
    }else if (usuarioLogeado.tipo =="pintor"){
    
        let liMisPinturas =  document.createElement("li")
        liMisPinturas.innerHTML = `<a href="misPinturas.html">Mis Pinturas</a>`
    
        navbar.appendChild(liMiPinturas)
    }

    let liCerrarSesion = document.createElement("li")
    liCerrarSesion.innerHTML = `<a href="#" id="cerrarSesion">Log Out</a>`

    navbar.appendChild(liCerrarSesion)

    let liRegistro = document.getElementById("registro")
    let liLogin = document.getElementById("login")
    
    navbar.removeChild(liRegistro)
    navbar.removeChild(liLogin)


    let cerrarSesion = document.getElementById("cerrarSesion")
    cerrarSesion.addEventListener("click", (e) =>{
    e.preventDefault();

    localStorage.removeItem("sesion")
    window.location.href = "index.html";
    });

}

