# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
k = set()
d = {} 
for i in range(n):
    s = input()
    k.add(s)
    if s in d:
       d[s] += 1
    else:
        d[s] = 1
print(len(k))
for key in d.keys():
    print(d[key], end = " ")