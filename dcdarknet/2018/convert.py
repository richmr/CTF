def bitsToArray(val, sz = 32):
	outbits_str = bin(val)[2:]
	outbits_str = "0"*(sz-len(outbits_str)) + outbits_str
	outbits = [0 for i in range(sz)]
	index = sz-1
	for i in range(len(outbits_str)):
		outbits[index] = int(outbits_str[i])
		index -= 1
	return outbits