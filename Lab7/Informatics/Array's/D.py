n = int(input())
l = list(map(int, input().split()))
counter = 0
for i in range(n-1):
    if l[i] < l[i+1]:
       counter+=1
print(counter)