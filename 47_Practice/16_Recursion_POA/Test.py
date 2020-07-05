import unittest
from ProductofArray import productofarray

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(productofarray([1,2,3,10]), 60)

	def test_case_2(self):
		self.assertEqual(productofarray([1,2,3]), 6)

if __name__=='__main__':
	unittest.main()