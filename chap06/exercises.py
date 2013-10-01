#Author: Anne Wilkinson

def is_power(a, b):
	if a == 1:
		return True
	elif a % b != 0:
		return False 
	else:
	    return is_power(a/b, b)


print is_power(4, 6)

def gcd(a,b):
	"""Computes the greatest common denominator
	of two numbers"""
	if a > b:
		c = a
		d = b
		a = d
		b = c
	elif b == 0:
		return a
	elif a == b:
		return a
	else:
		r = a%b
		return gcd(a,r) 

print gcd(2, 4)

