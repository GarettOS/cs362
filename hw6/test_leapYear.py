import unittest
import leapYear

class TestStringMethods(unittest.TestCase):
   def test_leap1(self):
      self.assertEqual(leapYear.leapYear(4), "Not Leap Year")

   def test_leap2(self):
      self.assertEqual(leapYear.leapYear(-1), "Not Leap Year")

   def test_leap3(self):
      self.assertEqual(leapYear.leapYear(2000), "Leap Year")

if __name__ == '__main__':
   unittest.main()

