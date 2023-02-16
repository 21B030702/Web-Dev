function isEmpty(obj){
    for (let x in obj){
        return false;
    }
    return true;
}

let schedule = {};

alert( isEmpty(schedule) );

schedule["8:30"] = "get up";

alert( isEmpty(schedule) );