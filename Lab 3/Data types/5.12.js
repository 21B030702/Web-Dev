function unique(arr) {
    const un = [];
    for (let x of arr){
        if (!un.includes(x)){
            un.push(x);
        }
    }
    return un;
}
  
  let strings = ["Hare", "Krishna", "Hare", "Krishna",
    "Krishna", "Krishna", "Hare", "Hare", ":-O"
  ];
  
  alert( unique(strings) ); // Hare, Krishna, :-O