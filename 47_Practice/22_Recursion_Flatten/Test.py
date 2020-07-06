import unittest
from Flatten import flatten

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(flatten([[1,2],3,[4,5]]), [1,2,3,4,5])

	def test_case_2(self):
		self.assertEqual(flatten([1,2,3,[4,5]]), [1,2,3,4,5])

if __name__=='__main__':
	unittest.main()
