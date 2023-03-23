n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    if l[i] >= 0 and l[i+1] >= 0 or l[i] < 0 and l[i+1] < 0:
       print("YES")       
       exit()
print("NO")