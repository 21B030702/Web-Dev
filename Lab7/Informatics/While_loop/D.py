n = int(input())
while True:
    if n % 2 == 0:
       n/=2
    elif n % 2 == 1 and n == 1:
         print("YES")
         break
    else:
        print("NO")
        break