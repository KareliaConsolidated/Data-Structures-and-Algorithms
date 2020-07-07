import unittest
from CapitalizeFirst import capitalizefirst

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(capitalizefirst(['car', 'taco', 'banana']), ['Car', 'Taco', 'Banana'])

if __name__=='__main__':
	unittest.main()
