/*var name = "Pedro"

let dodge = {
  pneu: "borracha",
  padrão: "Completa",
  completa: true
}

const minhaLista = [
  name,
  dodge,
  {
    animal:'cat',
    age: 3},
  "monkey"
]

console.log(minhaLista[1].pneu)

let a = '10
let b = 10
if(a===b){
  console.log('Iguais')
}
else(console.log('Diferentes'))*/

/*number = prompt("Insira o número:")
if(number%2==0){
    console.log("Par")
}else(console.log("Ímpar"))*/

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
