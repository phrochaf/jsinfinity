function valorInput() {
    // Obtém o elemento input pelo ID
    var inputElement = document.getElementById('Input');

    // Obtém o valor do input
    var valorInput = inputElement.value;


    // Exibe o valor no console
    var lista = document.getElementById('lista');

    var novoItem = document.createElement('li');

    novoItem.textContent = valorInput;

    lista.appendChild(novoItem);

    inputElement.value = '';

    
}