import unittest
from CapitalizeWords import capitalizeWords

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(capitalizeWords(['i','am','learning','data','science']), ['I', 'AM', 'LEARNING', 'DATA', 'SCIENCE'])
		
if __name__=='__main__':
	unittest.main()
