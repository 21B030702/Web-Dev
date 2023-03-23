def parrot_trouble(talking, hour):
   if hour < 7 and talking == True or hour > 20 and talking == True:
      return True
   else:
      return False
