n = int(input())
i = 0
sum = 0
while n!=0:
    sum += (n%10)*pow(2, i)
    n //= 10
    i+=1
print(sum)