
__metaclass__ = type

class Person:

	def setName(self, name):
		self.name = name

	def getName(self):
			return self.name

	def greet(self):
		print "Hello, world! I'm %s." %self.name


class Secretive:

	def __inaccessible(self):
		print "Bet you can't see me..."

	def accessible(self):
		print "The secret message is: "
		self.__inaccessible()



class StudentCount:
	__count = 0
	def init(self):
		self.count = 1
	def show(self):
		return self.count
	def inc(self):
		self.count += 1


# Filters spam
class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self): #override init function in Filter
		self.blocked = ['SPAM']