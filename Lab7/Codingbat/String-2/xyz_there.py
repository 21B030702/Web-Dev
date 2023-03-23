def xyz_there(str):
    if str.startswith(".xyz"):
       return False
    elif str.endswith(".xyz"):
       return False
    else :
       return "xyz" in str