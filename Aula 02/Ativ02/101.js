peso = prompt("Insira seu peso(em kg):")
altura = prompt("Insira sua altura(em m):")
imc= peso/(altura*altura)

console.log(`Seu IMC é ${imc}`)
if (imc < 18.5){
    console.log("Você está abaixo do peso")
} else if (imc >= 18.5 && imc < 24.9){
    console.log("Você está com o peso normal")
} else if (imc >= 24.9 && imc < 29.9){
    console.log("Você está com sobrepeso")
} else if (imc >= 29.9 && imc < 39.9){
    console.log("Você está Obeso")
} else if (imc >= 39.9){
    console.log("Você está com Obesidade grave")
} else (console.log("Valores inválidos"))
