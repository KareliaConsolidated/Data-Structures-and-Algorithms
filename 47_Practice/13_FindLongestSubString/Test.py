import unittest
from FindLongestSubString import FindLongestSubString


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(FindLongestSubString(''), 0)

	def test_case_2(self):
		self.assertEqual(FindLongestSubString('thisisawesome'), 6)

	def test_case_3(self):
		self.assertEqual(FindLongestSubString('thecatinthehat'), 7)

	def test_case_4(self):
		self.assertEqual(FindLongestSubString('bbbbb'), 1)

	def test_case_5(self):
		self.assertEqual(FindLongestSubString('longestsubstring'), 8)		

	def test_case_6(self):
		self.assertEqual(FindLongestSubString('thisishowwedoit'), 6)			

if __name__=='__main__':
	unittest.main()