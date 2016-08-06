def factorial(num = 10):
	if num > 0:
		return num * factorial(num-1)
	else :
		return 1

def power(num, exp):
	if exp > 0:
		return num * power(num, exp - 1)
	else:
		return 1

