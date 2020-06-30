import unittest
from MinSubArrayLen import MinSubArrayLen


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(MinSubArrayLen([2,3,1,2,4,3], 7), 2)

	def test_case_2(self):
		self.assertEqual(MinSubArrayLen([2,1,6,5,4], 9), 2)

	def test_case_3(self):
		self.assertEqual(MinSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52), 1)

	def test_case_4(self):
		self.assertEqual(MinSubArrayLen([1,4,16,22,5,7,8,9,10], 55), 5)

	def test_case_5(self):
		self.assertEqual(MinSubArrayLen([4,3,3,8,1,2,3], 11), 2)

	def test_case_6(self):
		self.assertEqual(MinSubArrayLen([1,4,16,22,5,7,8,9,10], 95), 0)

	def test_case_7(self):
		self.assertEqual(MinSubArrayLen([1,4,16,22,5,7,8,9,10], 39), 3)

	def test_case_8(self):
		self.assertEqual(MinSubArrayLen([1,4,16,22,5,7,8,9,39], 39), 1)

	def test_case_9(self):
		self.assertEqual(MinSubArrayLen([39], 39), 1)

if __name__=='__main__':
	unittest.main()