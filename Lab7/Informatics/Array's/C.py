n = int(input())
l = list(map(int, input().split()))
counter = 0
for i in l:
    if i > 0:
       counter+=1
print(counter)