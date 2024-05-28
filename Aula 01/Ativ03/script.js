let idade = parseInt(prompt("Digite sua idade:"))
let checkBday = prompt("Você já fez aniversário esse ano? (S ou N)")
ano = 2024 - idade
if (checkBday == 'S') {
    
    console.log(`Você nasceu em ${ano}`)
    
} else {
    ano -=1
    console.log(`Você nasceu em ${ano}`)
}