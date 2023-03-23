def not_string(str):
   x = str.split()
   if x[0] == "not":
      return str
   else:
      return "not" + " " + str