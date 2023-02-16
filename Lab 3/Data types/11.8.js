function formatDate(date){
    const now = new Date();
    let dif = new Date(now - date);
    if (dif < 1000){
        return "right now";
    }
    else if (dif < 1000 * 60){
        return `${dif.getSeconds()} sec. ago`;
    }
    else if (dif < 1000 * 60 * 60){
        return `${dif.getMinutes()} min. ago`;
    }
    else {
        const d = ['0' + date.getDate(), '0' + (date.getMonth() + 1), '' + date.getFullYear(), 
        '0' + date.getHours(), '0' + date.getMinutes()].map(val => val.slice(-2));
        return d.slice(0, 3).join('.') + ' ' + d.slice(3).join(':');
    }
}