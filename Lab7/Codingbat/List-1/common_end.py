def common_end(a, b):
  for i in range(len(a)):
      for j in range(len(b)):
          if a[i] == b[j] and i == 0 and j == 0 or a[i] == b[j] and i == len(a)-1 and j == len(b)-1:
             return True
  return False