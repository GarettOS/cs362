def testAddition(a, b):
   # test if adding 2 negative numbers
   if(a < 0 and b < 0):
      print("adding 2 negative numbers")
   return

def testSubtraction(a, b):
   # test if subtracting a positive and a negative
   if ((a > 0 and b < 0) or (a < 0 and b > 0)):
      print("Subtracting a positive and a negative number")
   return

def testMultiplication(a, b):
   # test if multiplying decimals
   if (a % 1 != 0 or b % 1 != 0):
      print("You are multiplying decimals")
   return 

def testDivision(a, b):
   # test if dividing by 0
   if (b == 0):
      print("Dividing by 0, answer cannot be found")
   return 0

