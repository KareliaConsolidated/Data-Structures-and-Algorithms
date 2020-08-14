# ---------------------- PROBLEM 46 ----------------------------------#
# n computing, a hash table (hash map) is a data structure that implements an 
# associative array abstract data type, a structure that can map keys to values. 
# A hash table uses a hash function to compute an index, also called a hash code, 
# into an array of buckets or slots, from which the desired value can be found.
class Hash:
	def __init__(self, size = 53):
		self.KeyVal = [None] * size

	def hash(self, key):
		total, WEIRD_PRIME = 0, 31
		for i in range(min(len(key), 100)):
			char = key[i]
			value = ord(char) - 96
			total = (total * WEIRD_PRIME + value) % len(self.KeyVal)
		return total

	def set(self, key, val):
		hashed_key = self.hash(key)
		if self.KeyVal[hashed_key] is None:
			self.KeyVal[hashed_key] = []
		self.KeyVal[hashed_key].append([key, val])
		return self.KeyVal[hashed_key]

	def get(self, key):
		hashed_key = self.hash(key)
		idx = self.KeyVal[hashed_key]
		if idx is not None:
			for pair in idx:
				if key == pair[0]:
					return pair[1]
		return None

	def keys(self)		:
		keyArr = []
		pair_list = self.KeyVal
		for lst in pair_list:
			if lst:
				for key in lst:
					if key[0] not in keyArr: keyArr.append(key[0])
		return keyArr

	def values(self)		:
		valArr = []
		pair_list = self.KeyVal
		for lst in pair_list:
			if lst:
				for val in lst:
					if val[1] not in valArr: valArr.append(val[1])
		return valArr

hashMap = Hash(13)		
print(hashMap.hash("goodbye")) # 9
print(hashMap.set('red', '#FF0000')) # [['red', '#FF0000']]
print(hashMap.set('white', '#FF0000')) # [['white', '#FF0000']]
print(hashMap.get('red')) # FF0000
print(hashMap.keys()) # ['white', 'red']
print(hashMap.values()) # ['#FF0000']