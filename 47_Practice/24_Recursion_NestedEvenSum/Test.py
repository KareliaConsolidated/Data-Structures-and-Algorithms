import unittest
from NestedEvenSum import NestedEvenSum

dict1 = {
	'outer': 2,
	'obj': {
	'inner': 2,
	'otherObj': {
	'superInner': 2,
	'notANumber': True,
	'alsoNotANumber': "Yup"
	}
	}
}

dict2 = {
	'a': 2,
	'b': {'b':2, 'bb':{'b':3, 'bb': {'b':2}}},
	'c': {'c': {'c':2}, 'cc': 'ball', 'ccc':5},
	'd':1,
	'e': {'e': {'e':2}, 'ee': 'car'}
}

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(NestedEvenSum(dict1), 6)

	def test_case_2(self):
		self.assertEqual(NestedEvenSum(dict2), 10)
		
if __name__=='__main__':
	unittest.main()
