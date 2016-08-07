def checkIndex(key):
	"""
	Check for acceptable key,

	If the key is not an integer or the key is less than 0,
	raise the appropriate error
	"""
	if not isinstance(key, (int,long)): raise TypeError
	if key<0: raise IndexError

class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self, key):
		checkIndex(key)

		try: return self.changed[key]
		except KeyError:
			return self.start + key*self.step

	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value
		

