function readNumber(){  
    let a;
    do{
        a = prompt("number");
        if (a == null || a == ""){
            return null;
        }
    }         
    while(!isFinite(a))
    return +a;         
}