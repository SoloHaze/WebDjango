const form = document.getElementById("formLogin");
form.addEventListener("submit", (e) => {

    const email= document.getElementById("email")
    const password = document.getElementById("password")

    if(!email.value.trim() || !password.value.trim()){
        alert("LOS CAMPOS SON OBLIGATORIOS");
        return;
    }

    let usuariosLocal = JSON.parse(localStorage.getItem("usarioos"))
    let flag = false;
    usuariosLocal.array.forEach(u => {
        if(u.email == email.value && u.password == password.value){
            
            bandera= true
            localStorage.setItem("sesion",JSON.stringify(u) )
        }
    });

    if(flag){
        alert("Login Exitoso!")
        window.location.href = "index.html";
        return;

    }else{

        alert("usuario o contraseña incorrecto!")

    }


});