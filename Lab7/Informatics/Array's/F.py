n = int(input())
l = list(map(int, input().split()))
counter = 0
for i in range(n//2, n-1, 1):
    if l[i] > l[i-1] and l[i] > l[i+1]:
       counter += 1
    if n == 3:
       print(counter)
       exit()
for i in range(n//2-1, 0, -1):
    if l[i] > l[i-1] and l[i] > l[i+1]:
        counter+=1
print(counter)