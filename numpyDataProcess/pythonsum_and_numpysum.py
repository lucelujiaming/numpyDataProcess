# coding: utf-8

def pythonsum(n): 
	a = list(range(n))
	b = list(range(n))
	c = [] 
	for i in range(len(a)): 
		a[i] = i ** 2 
		b[i] = i ** 3 
		c.append(a[i] + b[i]) 
	return c

print("pythonsum : ", pythonsum(5))

import numpy
def numpysum(n): 
	a = numpy.arange(n) ** 2 
	b = numpy.arange(n) ** 3 
	c = a + b 
	return c

print("numpysum : ", numpysum(5))
