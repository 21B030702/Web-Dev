function getLastDayOfMonth(year, month){
    const day = new Date(year, month + 1, 0);
    return day.getDate();
}