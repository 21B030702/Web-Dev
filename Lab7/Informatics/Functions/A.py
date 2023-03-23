def min(x, y, z, w):
    if x < y:
       m = x
    else:
       m = y
    if z < w:
       h = z
       if m > h:
          print(h)
       else:
          print(m)
    else:
       h = w
       if m > h:
          print(h)
       else:
          print(m)
a, b, c, d = map(int, input().split())
min(a, b, c, d)
