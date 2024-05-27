let saldo = 1000;

while (true) {
    let menu = prompt("BanKing:\n1. Ver Saldo\n2. Fazer Saque\n3. Fazer Depósito\n4. Sair");

    if  (menu === "1") {
        alert(`Seu saldo atual é: ${saldo}`);
    } else if  (menu === "2") {
        let saque = parseFloat(prompt("Digite o valor do saque:"));
        if (saque <= 0) {
            alert("Valor inválido. Tente novamente.");
        } else if (saque > saldo) {
            alert("Saldo insuficiente.");
        } else {
            saldo -= saque;
            alert(`Realizado com sucesso! Seu novo saldo é: ${saldo}`);
        }
    } else if  (menu === "3") {
        let deposito = parseFloat(prompt("Digite o valor a ser depositado:"));
        if (deposito <= 0) {
            alert("Valor inválido. Tente novamente.");
        } else {
            saldo += deposito;
            alert(`Depósito realizado com sucesso! Seu novo saldo é: ${saldo}`);
        }
    } else if  (menu === "4") {
        alert("Até logo!");
        break;
    } else {
        alert("Opção inválida. Tente novamente.");
    }
}