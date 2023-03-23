def close_far(a, b, c):
    if abs(a-b) >= 0 and abs(b-c) >= 2 and abs(a-b)!=abs(a-c) or abs(b-c) >= 0 and abs(a-b) >= 2 and abs(c-b)!=abs(c-a):
       return True
    else:
       return False
