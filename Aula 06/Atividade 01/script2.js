


function nVogais(palavra){
    let cont = 0;
    palavra = palavra.toLowerCase();
    
    for (let i=0; i <palavra.length; i++){
        console.log(palavra[i])

            if (palavra[i] == "a" || palavra[i] =="e" || palavra[i] =="i" || palavra[i] =="o" || palavra[i] =="u"){
                cont++
            };

    ;
    }
return cont;
};


console.log(nVogais("Problema"));



