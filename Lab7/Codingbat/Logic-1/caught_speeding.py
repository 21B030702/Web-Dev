def caught_speeding(speed, is_birthday):
    if speed <= 60 and is_birthday == False or speed <= 65 and is_birthday == True:
       return 0
    elif speed >= 61 and speed <= 80 and is_birthday == False or speed >= 66 and speed <= 85 and is_birthday == True:
       return 1
    elif speed > 80 and is_birthday == False or speed > 85 and is_birthday == True:
       return 2