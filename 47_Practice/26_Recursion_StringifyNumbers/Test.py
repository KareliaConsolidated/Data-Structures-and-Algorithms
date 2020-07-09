import unittest
from StringifyNumbers import stringifyNumbers

dict1 = {'num': 1,
		'test': [],
		'data': {
			'val': 4,
			'info':{
				'isRight': True,
				'random': 66
				}
			}
		}

dict_ans = {'num': "1",
		'test': [],
		'data': {
			'val': "4",
			'info':{
				'isRight': True,
				'random': "66"
				}
			}
		}

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(stringifyNumbers(dict1), dict_ans)
		
if __name__=='__main__':
	unittest.main()
