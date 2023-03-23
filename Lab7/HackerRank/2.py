N = int(input())
l = []
for i in range(N):
    s = input().split()
    if s[0] == "insert":
        a = int(s[1])
        b = int(s[2])
        l.insert(a, b)
    elif s[0] == "remove":
         g = int(s[1])
         l.remove(g)
    elif s[0] == "append":
         k = int(s[1])
         l.append(k)
    elif s[0] == "sort":
         l.sort()
    elif s[0] == "reverse":
         l.reverse()
    elif s[0] == "print":
         print(l)
    else:
         if len(l) > 0:
            l.pop()