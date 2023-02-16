function topSalary(salaries){
    let max = 0;
    let name = null;
    for (let [key, val] of Object.entries(salaries)){
        if (max < val){
            max = val;
            name = key;
        }
    }
    return name;
}

let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
  };