import unittest
from python.src import largest_number

class test_largest_num(unittest.TestCase):

	def test_a(self):
		self.assertEqual(5, largest_number.find(5,3,2))
		self.assertEqual(5, largest_number.find(5,2,3))
		
	def test_b(self):
		self.assertEqual(5, largest_number.find(3,5,2))
		self.assertEqual(5, largest_number.find(2,5,3))
		
	def test_c(self):
		self.assertEqual(5, largest_number.find(2,3,5))
		self.assertEqual(5, largest_number.find(3,2,5))
		
	def test_None(self):
		self.assertEqual(5, largest_number.find(5,5,5))
		self.assertEqual(5, largest_number.find(5,3,3))