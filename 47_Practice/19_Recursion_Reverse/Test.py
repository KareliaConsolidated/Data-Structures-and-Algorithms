import unittest
from Reverse import reverse

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(reverse('awesome'), 'emosewa')

	def test_case_2(self):
		self.assertEqual(reverse('rithmschool'), 'loohcsmhtir')

if __name__=='__main__':
	unittest.main()