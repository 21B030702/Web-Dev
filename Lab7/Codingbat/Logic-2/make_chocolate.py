def make_chocolate(small, big, goal):
    if small + 5*(big) < goal:
       return -1
    else:
        if 5*big > goal: 
            if goal % 5 == 0:
                return 0
            elif small < goal % 5:
                return -1
            elif small >= goal % 5:
                return goal % 5
        elif goal > 5*big:
            return goal - 5*big
        else:
            return goal % 5