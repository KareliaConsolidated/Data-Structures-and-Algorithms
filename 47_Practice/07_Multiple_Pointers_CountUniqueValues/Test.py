import unittest
from CountUniqueValues import CountUniqueValues

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(CountUniqueValues([1, 1, 1, 1, 1, 2]), 2)

	def test_case_2(self):
		self.assertEqual(CountUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]), 7)

	def test_case_3(self):
		self.assertEqual(CountUniqueValues([]), None)

	def test_case_4(self):
		self.assertEqual(CountUniqueValues([-2, -1, -1, 0, 1]), 4)


if __name__ == '__main__':
	unittest.main()