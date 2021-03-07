import unittest
import leapYear

class TestStringMethods(unittest.TestCase):
   def test_leap1(self):
      self.assertEqual(leapYear.leapYear(4), "Not Leap Year")

if __name__ == '__main__':
   unittest.main()

