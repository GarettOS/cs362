import unittest
import fizzbuzz

class TestStringMethods(unittest.TestCase):
   def test_fizz1(self):
      self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')

   def test_fizz2(self):
      self.assertEqual(fizzbuzz.fizzbuzz(20), 'Buzz')
   
   def test_fizz3(self):
      self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")

if __name__ == '__main__':
   unittest.main()
