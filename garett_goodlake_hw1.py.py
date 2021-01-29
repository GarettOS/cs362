# A python program that takes a year as input from the user, and returns whether or not it is a leap year

year = input("Enter a year: ")
year = int(year)

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
