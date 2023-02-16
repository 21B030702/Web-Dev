let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}
let sum = 0;
for (let x in salaries){
    sum += salaries[x];
}
alert( sum );