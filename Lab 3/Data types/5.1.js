function camelize(str){
    const arr1 = str.split('-');
    const arr2 = arr1.map((val, ind) => ind == 0 ? val : val[0].toUpperCase() + val.slice(1));
    str = arr2.join('');
    return str;
}