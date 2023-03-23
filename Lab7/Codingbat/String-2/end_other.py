def end_other(a, b):
    t = a.lower()
    s = b.lower()
    if len(a) > len(b):
       return t.endswith(s)
    else:
       return s.endswith(t)