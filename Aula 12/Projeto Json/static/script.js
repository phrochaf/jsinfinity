/*Não sei se era o que o projeto queria, mas usei um servidor flask para poder acessar o arquivo json,
visto que o navegador não permiti manipular arquivos locais por questões de segurança.*/

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('livroform');
    const lista = document.getElementById('lista').querySelector('tbody');
    const search = document.getElementById('search');
    const resultado = document.getElementById('resultado');

    async function carregarLivros() {
        try {
            const response = await fetch('http://127.0.0.1:5000/books');
            return await response.json();
        } catch (error) {
            return [];
        }
    }
    
    async function salvarLivros(livros) {
        await fetch('http://127.0.0.1:5000/books', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(livros)
        }).then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    }

    async function listarLivros() {
        const livros = await carregarLivros();
        lista.innerHTML = '';
        livros.forEach(livro => {
            const livroItem = document.createElement('tr');
            livroItem.classList.add('livro-item');
            livroItem.innerHTML = `
                <td>${livro.nome}</td>
                <td>${livro.autor}</td>
                <td>${livro.genero}</td>
                <td>${livro.ano}</td>
                <td>${livro.nota}</td>
            `;
            lista.appendChild(livroItem);
        });
    }

    // Adicionar um novo livro
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const nome = document.getElementById('nome').value;
        const autor = document.getElementById('autor').value;
        const genero = document.getElementById('genero').value;
        const ano = document.getElementById('ano').value;
        const nota = document.getElementById('nota').value;

        const livros = await carregarLivros();
        let novoLivro = {
            "nome": nome,
            "autor": autor,
            "genero": genero,
            "ano": ano,
            "nota": nota
        };

        livros.push(novoLivro);
        await salvarLivros(livros);
        listarLivros();

        alert('Livro cadastrado com sucesso!');
    });

    listarLivros();


    // Pesquisar um livro
    search.addEventListener('submit', async function(e) {
        e.preventDefault();
        const searchInput = document.getElementById('searchInput').value;
        const livros = await carregarLivros();
        resultado.innerHTML = '';
        lista.innerHTML = '';
        livros.forEach(livro => {
            if (livro.nome.includes(searchInput) || livro.autor.includes(searchInput) || livro.genero.includes(searchInput)) {
                const livroItem = document.createElement('tr');
                livroItem.classList.add('livro-item');
                livroItem.innerHTML = `
                    <td>${livro.nome}</td>
                    <td>${livro.autor}</td>
                    <td>${livro.genero}</td>
                    <td>${livro.ano}</td>
                    <td>${livro.nota}</td>
                `;
                resultado.appendChild(livroItem);
                listarLivros();
            
            } 
        });
    })


});