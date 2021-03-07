import unittest
import fizzbuzz

class TestStringMethods(unittest.TestCase):
   def test_fizz1(self):
      self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')

if __name__ == '__main__':
   unittest.main()
