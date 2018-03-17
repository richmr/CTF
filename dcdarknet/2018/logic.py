#!/usr/bin/python

from functools import reduce

def _not(bit):
	if (bit):
		return 0
	else:
		return 1
	
def _or(bits):
	# expects an array of bits
	if (len(bits) > 1):
		result = reduce((lambda x, y: x | y), bits)
		return result
	else:
		return bits[0]
		
def _and(bits):
	# expects an array of bits
	if (len(bits) > 1):
		result = reduce((lambda x, y: x & y), bits)
		return result
	else:
		return bits[0]

def _xor(bits):
		# expects an array of bits
	if (len(bits) > 1):
		result = reduce((lambda x, y: x ^ y), bits)
		return result
	else:
		return bits[0]
		
def _nand(bits):
		# expects an array of bits
	return _not(_and(bits))
	
def _nor(bits):
	return _not(_or(bits))

def _xnor(bits):
	return _not(_xor(bits))
	
def _switch(d0, d1, sw0):
	# if sw is high then picks d1
	# otherwise picks d0
	
	if (sw0):
		return d1
	else:
		return d0

