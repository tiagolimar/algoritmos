function confereIdade() {
    let idade = +prompt("Digite a sua idade: ");
    
    idade > 80 && console.log("Você é idoso");
    idade < 12 && console.log("Você é criança");
    idade >= 12 && idade <= 18 && console.log("Você é adolescente");
    idade > 18 && idade < 80 && console.log("Você é adulto");
}

function calculadora() {
    let num1 = +prompt("Digite o primeiro número: ");
    let num2 = +prompt("Digite o segundo número: ");
    let operador = prompt("Digite o operador ( + - / * ): ");
    
    operador == "+" && console.log(num1 + num2);
    operador == "-" && console.log(num1 - num2);
    operador == "/" && console.log(num1 / num2);
    operador == "*" && console.log(num1 * num2);
    
    !['+','-','/','*'].includes(operador) && console.log("Operador inválido");
    
    switch(operador){
        case "+": console.log(num1 + num2); break;
        default: console.log('Operação inválida'); break;
        case "-": console.log(num1 - num2); break;
        case "/": console.log(num1 / num2); break;
        case "*": console.log(num1 * num2); break;
    }
}

function testar(testes, variavel) {
    for (const key in testes) {
        const [min, max] = key.split("~").map(Number);
        if (
            (isNaN(min) || variavel >= min) && 
            (isNaN(max) || variavel < max)
        ) {
            console.log(testes[key]);
            return;
        }
    }
}

function confereIdade2() {
    let idade = +prompt("Digite a sua idade: ");

    let teste = {
        "~12": "Criança",
        "12~18": "Adolescente",
        "18~80": "Adulto",
        "80~": "Idoso",
    }
    
    testar(teste, idade);
}


function imc(){
    let teste = {
        "~18.5": "Abaixo do peso",
        "18.5~24.9": "Peso normal",
        "25~29.9": "Sobrepeso",
        "30~34.9": "Obesidade grau 1",
        "35~39.9": "Obesidade grau 2",
        "40~": "Obesidade grau 3",
    }

    let imc = +prompt("Digite o seu IMC: ");
    testar(teste, imc);
}