import unittest
import fullName

class testModule(unittest.TestCase):
   def test1(self):
      self.assertEqual(fullName.fullName("Garett", "Goodlake"), "Garett Goodlake")

   def test2(self):
      self.assertNotEqual(fullName.fullName("Randy", "Lahey"), "Julian Ricky")

   def test3(self):
      self.assertTrue(str(fullName.fullName("Randy", "Lahey")))


