import unittest
from SomeRecursive import someRecursive, isOdd, isEven

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(someRecursive([1,2,3,4], isOdd), True)

	def test_case_2(self):
		self.assertEqual(someRecursive([4,6,8,9], isOdd), True)

	def test_case_3(self):
		self.assertEqual(someRecursive([4,6,8], isOdd), False)

	def test_case_4(self):
		self.assertEqual(someRecursive([4,6,8], isEven), True)		

if __name__=='__main__':
	unittest.main()
