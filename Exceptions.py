	
while True:
	try: 
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		print x/y
		break
	except:
		print "The second number can't be zero!"


while True:
	try:
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		print x/y
		break
	except (ZeroDivisionError, TypeError, NameError),e:
		print e
	else:
		print 'All is well!'