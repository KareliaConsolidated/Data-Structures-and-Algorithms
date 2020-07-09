import unittest
from CollectStrings import collectstrings

dict1 = {
	"stuff": "foo",
	"data":{
	"val":{
	"thing":{
	"info":"bar",
	"moreInfo":{
	"evenMoreInfo":{
	"weMadeIt":"baz"
	}
	}
	}
	}
	}
}

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(collectstrings(dict1), ["foo", "bar", "baz"])
		
if __name__=='__main__':
	unittest.main()
