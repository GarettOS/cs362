import unittest
import cubeVolume
import math

class testModule(unittest.TestCase):
   def test1(self):
      self.assertEqual(cubeVolume.volume(5,2,1), 10)
   
   def test2(self):
      self.assertEqual(cubeVolume.volume(-1,5,3), -15)

   def test3(self):
      self.assertEqual(cubeVolume.volume(2.5,5,5), 62.5)
