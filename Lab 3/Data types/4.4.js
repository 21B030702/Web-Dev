function sumInput(){
    let arr = [];
    let sum = 0;
    a = prompt("val");
    while(isFinite(a)) {
        arr.push(+a);
        a = prompt("val");
        if (a == null || a == ""){
            break;
        }
    }
    for (let i of arr){
        sum += i;
    }
    return sum;
}