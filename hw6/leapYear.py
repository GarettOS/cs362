def leapYear(x):
   if (x < 0):
      return "Not Leap Year"
   if (x % 4 == 0):
      if (x % 100 == 0):
         if (x % 400 == 0):
            return "Leap Year"
         else:
            return "Not Leap Year"
      else:
         return "Not Leap Year"
   else:
      return "Not Leap Year"
