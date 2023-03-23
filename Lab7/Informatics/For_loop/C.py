import math
a = int(input())
b = int(input())
c = int(math.sqrt(b)+1)
for i in range(math.ceil(math.sqrt(a)), c):
    print(i**2, end = " ")