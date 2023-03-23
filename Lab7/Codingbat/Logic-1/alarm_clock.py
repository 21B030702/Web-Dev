def alarm_clock(day, vacation):
    if day == 0 and vacation == False or day == 6 and vacation == False:
       return "10:00"
    elif day >= 1 and day <= 5 and vacation == False:
       return "7:00"
    elif day >= 1 and day <= 5 and vacation == True:
       return "10:00"
    elif day == 0 and vacation == True or day == 6 and vacation == True:
       return "off"