def no_teen_sum(a, b, c):
    sum = 0
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    for i in range(len(l)):
        if l[i] >= 13 and l[i] <= 19 and l[i]!=15 and l[i]!=16:
           sum += 0
        else:
           sum += l[i]
    return sum