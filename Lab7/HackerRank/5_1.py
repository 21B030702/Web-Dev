for i in range(1,int(input())+1):
    print(*range(1,i+1), *range(i-1, 0, -1), sep="")