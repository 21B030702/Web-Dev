n, m = map(int, input().split())
l = list(map(int, input().split()))
count_happiness = 0
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
for i in l:
    if i in setA:
       count_happiness += 1
    elif i in setB:
       count_happiness -= 1
print(count_happiness)
        