const button = document.querySelector('button')

button.addEventListener('click', function(e){
    console.log(e)

    document.querySelector('h1').classList.toggle('oculto')
} )