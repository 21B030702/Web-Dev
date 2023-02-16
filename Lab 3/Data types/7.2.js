function aclean(arr){
    const m = new Map();
    for (let x of arr){
        m.set(x.toLowerCase().split("").sort().join(""), x);
    }
    return Array.from(m.values());
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

alert( aclean(arr) ); // "nap,teachers,ear" or "PAN,cheaters,era"