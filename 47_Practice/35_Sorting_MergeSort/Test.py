import unittest
from MergeSort import MergeSort

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(MergeSort([8,1,2,3,4,5,6,7]), [1, 2, 3, 4, 5, 6, 7, 8])

	def test_case_2(self):
		self.assertEqual(MergeSort([5,4,3,1,2]), [1,2,3,4,5])

	def test_case_3(self):
		self.assertEqual(MergeSort([]), [])

	def test_case_4(self):
		self.assertEqual(MergeSort([5,4,3,1,2,-6]), [-6, 1, 2, 3, 4, 5])
		
if __name__=='__main__':
	unittest.main()