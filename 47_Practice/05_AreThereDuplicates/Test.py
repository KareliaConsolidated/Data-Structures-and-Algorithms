import unittest
from AreTheDuplicates import arethereduplicates

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(arethereduplicates(1, 2, 3), False)

	def test_case_2(self):
		self.assertEqual(arethereduplicates(2, 2, 1), True)

	def test_case_3(self):
		self.assertEqual(arethereduplicates('a', 'b', 'c', 'c'), True)
		
if __name__ == '__main__':
	unittest.main()