def init(data):
	data['first'] = {}
	data['second'] = {}
	data['last'] = {}


def lookup(data, label, name):
	return data[label].get(name)

def store(data, fullname):
	names = fullname.split()
	if len(names) == 1: 
		names.insert(1, "")
		names.insert(2, "")
	elif len(names) == 2:
		names.insert(1, "")

	labels = ['first','second','last']

	for label, name in zip(labels, names):
		people = lookup(data, label, name)
		if people:
			people.append(fullname)
		else:
			data[label][name] = [fullname]
def showall(data):
	print data
