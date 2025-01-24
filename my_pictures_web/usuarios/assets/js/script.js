let nombrePintura = "";
let autor = "";
let precio = 0;
let descripcion = "";
let tecnicaUsada = "";

let pinturasArray = [];


pinturasArray.push(nombrePintura);
pinturasArray.push(descripcion);
pinturasArray.push(precio);
pinturasArray.push(autor);
pinturasArray.push(tecnicaUsada);


pinturasArray[0] = "";//Aqui va el input desde el formulario de agregar pintura
pinturasArray[1] = "";

//function para agregar a un array las variable devueltas por el fomrulario de agregar pintura
let agregarPintura = (nombrePintura,descripcion,precio,autor,tecnicaUsada) =>{
    let agregarPinturaArray = [];

    pinturasArray.push(nombrePintura);
    pinturasArray.push(descripcion);
    pinturasArray.push(precio);
    pinturasArray.push(autor);
    pinturasArray.push(tecnicaUsada);

    return agregarPinturaArray;

}
console.log(agregarPintura(nombrePintura,descripcion,precio,autor,tecnicaUsada));



//con el indexOf se buscara cada pintura por su nombre con la barra de busqueda



//tablas para guardar productos, en este caso pinturas
let pinturas = [
    {
        pintura: "Arbol de la creacion", descripcion: "arbolito", precio: 5000,autor: "Desconocido", tecnicaUsada: "Óleo",estado: "aprobado",
    },
    {
        pintura: "Arbol de la creacion", descripcion: "arbolito", precio: 5000,autor: "Desconocido", tecnicaUsada: "Óleo",estado: "aprobado",
    },
    {
        pintura: "Arbol de la creacion", descripcion: "arbolito", precio: 5000,autor: "Desconocido", tecnicaUsada: "Óleo",estado: "aprobado"
    }
]

if(!localStorage.getItem("pinturas")){
    localStorage.setItem("pinturas", JSON.stringify(pinturas))
}
function crearTabla(){
    const principal = document.getElementById("principal");
    
    const tabla = document.createElement("table");
    tabla.classList.add("table","table-striped","table-hover");
    
    tabla.innerHTML = `
        <thead>
            <th>Pintura</th>
            <th>Descripcion</th>
            <th>Precio</th>
            <th>Autor</th>
            <th>Tecnica Usada</th>
            <th>Dolar</th>
        </thead>
        <tbody id="cuerpo-tabla"></tbody>
    `;

    principal.appendChild(tabla);
}

function cargarPinturas(){



    let valorDolarrr = 0;

    //consumir una api:
    fetch("https://mindicador.cl/api")
    .then(response => response.json())//El response se convnierte en json
    //.then(data => console.log(data))//así se pide toda la data entregada de la api
    .then(data => {
        console.log(data.dolar.valor)
        valorDolarrr = data.dolar.valor;

            
        const cuerpoTabla = document.getElementById("cuerpo-tabla");
        cuerpoTabla.innerHTML = '';
        let pinturasLocal = JSON.parse(localStorage.getItem("pinturas"));
        pinturasLocal.forEach(p => {
            //console.log(p);
            if(p.estado == 'aprobado'){
                const filaTabla = document.createElement("tr");
                filaTabla.innerHTML = `
                    <td>${p.pintura}</td>
                    <td>${p.descripcion}</td>
                    <td>${p.precio}</td>
                    <td>${p.autor}</td>
                    <td>${p.tecnicaUsada}</td>
                    <td>US$ ${(p.precio / valorDolarrr).toFixed(2)}</td>
                
                `;
        
                cuerpoTabla.appendChild(filaTabla);


            }

    })

        
    });


    const cuerpoTabla = document.getElementById("cuerpo-tabla");



    cuerpoTabla.innerHTML = '';
    let pinturasLocal = JSON.parse(localStorage.getItem("pinturas"));
    pinturasLocal.forEach(p => {
        //console.log(p);
        if(p.estado == 'aprobado'){
            const filaTabla = document.createElement("tr");
            filaTabla.innerHTML = `
                <td>${p.pintura}</td>
                <td>${p.descripcion}</td>
                <td>${p.precio}</td>
                <td>${p.autor}</td>
                <td>${p.tecnicaUsada}</td>
            
            `;
    
            cuerpoTabla.appendChild(filaTabla);


        }

    })

}

crearTabla();
cargarPinturas();

//fomrulario para agregar pinturas
const formulario = document.getElementById("formulario");
formulario.addEventListener("submit", (e)=>{
    e.preventDefault();//prevetnDefault, evita la recarga de la pagina cdo se da click al submit

    const nombre = document.getElementById("nombre");
    const precio = document.getElementById("precio");

    if(!nombre.value().trim()){
        alert('El nombre de la pintura es obligatorio');
        return;
    }else if(!precio.value().trim()){
        alert('El campo precio es obligatorio')
        return;
    }
    let pinturasLocal = JSON.parse(localStorage.setItem("pintura"));

    let pintura = {id: pinturasLocal.length+1,pintura: nombre.value.trim(),
          descripcion: "arbolito",
          precio: precio.value().trim(), 
          autor: "Desconocido",
          tecnicaUsada: "Óleo",
          estado: "aprobado"
    }
    pinturasLocal.push(pintura)
    localStorage.setItem("pinturas", JSON.stringify(pinturasLocal))

    pinturas.push();
    alert('pintura agregada con éxito');
    cargarPinturas();

    nombre.innerText = '';
    precio.innerText = '';
    
});

