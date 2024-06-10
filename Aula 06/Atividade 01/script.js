
let cont = 0;

function nVogais(palavra){
    
    for (let i=0; i <palavra.length; i++){
        console.log(palavra[i])

            if (palavra[i] == "a" || palavra[i] =="e" || palavra[i] =="i" || palavra[i] =="o" || palavra[i] =="u"){
                cont++
            };

    ;
    }};


nVogais("Beterraba");
console.log(cont);