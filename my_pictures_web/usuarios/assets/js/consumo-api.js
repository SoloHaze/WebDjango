let valorDolar = 0;

//consumir una api:
fetch("https://mindicador.cl/api")
.then(response => response.json())//El response se convnierte en json
//.then(data => console.log(data))//así se pide toda la data entregada de la api
.then(data => {
    console.log(data.dolar.valor)
    valorDolar = data.dolar.valor;
    
});


