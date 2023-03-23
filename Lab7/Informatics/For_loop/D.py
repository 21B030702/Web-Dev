x = int(input())
d = int(input())
sum = 0
while x:
    if x % 10 == d:
       sum += 1
    x //= 10
print(sum)