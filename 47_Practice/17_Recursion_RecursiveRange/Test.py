import unittest
from RecursiveRange import recursiveRange

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(recursiveRange(6), 21)

	def test_case_2(self):
		self.assertEqual(recursiveRange(10), 55)

if __name__=='__main__':
	unittest.main()