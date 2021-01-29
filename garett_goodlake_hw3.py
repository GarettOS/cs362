# A python program that takes a year as input from the user, and returns whether or not it is a leap year

while 1:
   try:
      year = int(input("Enter a year:" ))
      if(year < 0):
         raise ValueError
      break
   except ValueError:
      print("Enter something valid plz!!!!!!!!!!!")

      

if (year % 4 == 0):
   if(year % 100 == 0):
      if(year % 400 == 0):
         print(year, "is a leap year")
      else:
         print(year, "is not a leap year")
   else:
      print(year, "is a leap year")
else:
      print(year, "is not a leap year")
