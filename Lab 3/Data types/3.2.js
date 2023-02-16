function checkSpam(str){
    let x = str.search(/viagra/i);
    let y = str.search(/XXX/i);
    if (x != -1 || y != -1)
        return true;
    return false;
}