//Se manejara el registro  eusuario

let usuarioos= [

    {nombre: "admin", email: "admin@gmail.com", password: "admin123", tipo: "admin"},
    {nombre: "aron", email: "aron@gmail.com", password:"hola", tipo: "admin"},
    {nombre: "aronUser", email: "aronUser@gmail.com", password:"holaUser", tipo: "usuarioo"},
    
    
]
if(!localStorage.getItem("usuarioos")){
    localStorage.setItem("usuarioos", JSON.stringify(usuarioos))

}

const formulario = document.getElementById("formRegistro");
formulario.addEventListener("submit", (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const repetirContra = document.getElementById("confirmPassword");

    if(!nombre.value.trim()){
        alert("El nombre es requerido");
        return;
    }else if(!email.value.trim()){
        alert("El email es requerido");
        return;
    }else if(!password.value.trim()){
        alert("La contraseña es requerido");
        return;
    }else if(!repetirContra.value.trim()){
        alert("La confirmacin de la contraseña es requerido");
        return;
    }else if (password.value.trim() != repetirContra.value.trim()){
        alert("Las contraseñas no coinciden")
        return;
    }

    let usuarioo ={

        nombre: nombre.value,
        email: email.value,
        password: password.value,
        tipo: "pintor"

    }

    let usuarioosLocal = JSON.parse(localStorage.getItem("usuarioos"));
    usuarioosLocal.push(usuarioo);
    localStorage.setItem("usuarioos",JSON.stringify(usuarioosLocal))
    alert("Usuario Registrado")
    
    window.location.href = "login.html";


});



