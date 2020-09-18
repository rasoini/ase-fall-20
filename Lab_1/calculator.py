#calculator.py

def sum(m, n):
	#TODO
	res = m
	if (n > 0):
		while n > 0:
			res = res + 1
			n = n - 1
	else:
		while n < 0:
			res = res - 1
			n = n + 1
	return res


def divide(m, n):
	if n == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	res = 0
	mabs = abs(m)
	nabs = abs(n)
	while mabs >= nabs:
		res = res + 1
		mabs = mabs - nabs
	if (m < 0 and n < 0) or (m > 0 and n > 0) :
		return res
	else:
		return -1 * res


