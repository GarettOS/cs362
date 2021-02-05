import unittest
import avgInList

if __name__ == "__main__":
   IIittest.main(verbosity=2)

class testModule(unittest.TestCase):
   def test1(self):
      self.assertEqual(avgInList.avgInList([5, 3, 2, 1]), 2.75)

   def test2(self):
      self.assertEqual(avgInList.avgInList([-10, -5, -4, 4]), -3.75)

   def test3(self):
      self.assertEqual(avgInList.avgInList([]), 0) 
