document.addEventListener('DOMContentLoaded', () => {
    let form = document.querySelector('form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const nome = document.getElementById('nome').value;
    const autor = document.getElementById('autor').value;
    const genero = document.getElementById('genero').value;
    const ano = document.getElementById('ano').value;
    const nota = document.getElementById('nota').value;
   
    console.log(nota); //teste

    let livro = {
        "nome":nome,
        "autor":autor,
        "genero":genero,
        "ano":ano,
        "nota":nota
    }

    let livroData = JSON.stringify(livro);
    console.log(livroData)


    fetch('https://dummyjson.com/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(livro)
    });


});

/*function handleSubmit(event){
    event.preventDefault();
    let formData = new FormData(form);
    let data = Object.fromEntries(formData);
    let jsonData = JSON.stringify(data);

     fetch("data.json").then(res => res.json()).then((dados) => console.log(dados));
        
}*/
})