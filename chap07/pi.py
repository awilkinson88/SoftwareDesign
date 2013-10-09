from math import *

def pi_est (k):
	"""Estimates pi based off of Newton's algorithim"""
	inv_pi = 0
	while True:
		a = (2*sqrt(2)/9801)
		num = factorial(4*k)*(1103+26390*k)
		denom = factorial(k)**4*396**(4*k)
		inv_pi = inv_pi + a*num/denom
		k = k + 1
		error = a*num/denom
		if error < 1e-15:
			print pi_est
			print error
			break
		pi_est = 1/inv_pi


pi_est(0)

