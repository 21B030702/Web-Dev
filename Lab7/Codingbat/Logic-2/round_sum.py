def round_sum(a, b, c):
    l = [a, b, c]
    sum = 0
    for i in l:
        if i % 10 >= 5:
           i = i//10 * 10 + 10
        else:
           i = i - (i % 10)
        sum += i
    
    return sum