def count_code(str):
    count = 0
    x={"co"+i+"e" for i in str}
    for i in x:
        if i in str:
           count += str.count(i)
           
    return count
