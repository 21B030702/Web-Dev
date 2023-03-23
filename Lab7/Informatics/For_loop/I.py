n = int(input())
sum = 0
i = 1
while i*i <= n:
    if n % i == 0:
       sum+=1
       if n // i != i:
          sum+=1
    i+=1
print(sum)