s = input()
i = 0
while i < len(s):
    count = 0
    while i <= len(s)-2 and s[i] == s[i+1]:
          count+=1
          i+=1
          
    count += 1 
    a = (count, int(s[i]))
    print(a, end = " ")
    i+=1