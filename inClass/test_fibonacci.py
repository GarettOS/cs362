import unittest
import fibonacci

class TestStringMethods(unittest.TestCase):

   # Base cases
   def test_fib1(self):
      self.assertEqual(fibonacci.fib(0), 0)

   def test_fib2(self):
      self.assertEqual(fibonacci.fib(1), 1)

   def test_fib3(self):
      self.assertEqual(fibonacci.fib(2), 1)
	
   def test_fib4(self):
      self.assertFalse(fibonacci.fib(-2))

if __name__ == '__main__':
   unittest.main()
