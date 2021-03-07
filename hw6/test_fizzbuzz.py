import unittest

class TestStringMethods(unittest.TestCase):
   def test_fizz1(self):
      self.assertEqual(fizzbuzz(3), "Fizz")

   def test_fizz2(self):
      self.assertEqual(fizzbuzz(21), "Fizz")

   def test_fizz3(self):
      self.assertEqual(fizzbuzz(5), "Buzz")

   def test_fizz3(self):
      self.assertEqual(fizzbuzz(10), "Buzz")

   def test_fizz4(self):
      self.assertEqual(fizzbuzz(30), "FizzBuzz")

   def test_fizz5(self):
      self.assertEqual(fizzbuzz(15), "FizzBuzz")

if __name__ == '__main__':
   unittest.main()
