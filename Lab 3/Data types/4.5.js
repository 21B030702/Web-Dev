function getMaxSubSum(arr){
    let max = 0;
    let sum = 0;
    for (let i = 0; i < arr.length; i++){
        sum += arr[i];
        if (sum < 0){
            sum = 0;
        }
        else if (sum > max){
            max = sum;
        }
    }
    return max;
}