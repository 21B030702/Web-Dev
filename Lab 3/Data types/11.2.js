function getWeekDay(date){
    let day = date.getDay();
    switch(day){
        case 0:
            return "SU";
        case 1:
            return "MO";
        case 2:
            return "TU";
        case 3:
            return "WE";
        case 4:
            return "TH";
        case 5:
            return "FR";
        case 6:
            return "SA";
    }
}
let date = new Date(2012, 0, 3);  // 3 Jan 2012
alert( getWeekDay(date) );        // should output "TU"