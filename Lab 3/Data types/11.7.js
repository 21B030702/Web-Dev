function getSecondsToTomorrow(){
    const date = new Date();
    return 60 * 60 * 24 - date.getSeconds() - date.getMinutes() * 60 - date.getHours() * 60 * 60;
}