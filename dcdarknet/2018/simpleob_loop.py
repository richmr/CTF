#!/usr/bin/python

from logic import _not, _or, _and, _nand, _xor, _xnor, _switch, _nor
import time

starttime = time.time()
runs = 0
for i in range(1000):
	runs += 1
	inbits_str = bin(0x5EFA570B)[2:]
	inbits_str = "0"*(32-len(inbits_str)) + inbits_str
	
	inbits = [0 for i in range(len(inbits_str))]
	
	index = 31
	for i in range(len(inbits_str)):
		inbits[index] = int(inbits_str[i])
		index -= 1
	
	outbits = [0 for i in range(len(inbits_str))]
	
	Din = inbits
	Dout = outbits
	
	Dout[31] = Din[30]
	
	Dout[30] = Din[31]
	Dout[29] = _not(Din[29])
	Dout[28] = _xor([Din[28], Din[27]])
	Dout[27] = _and([Din[28], Din[27]])
	Dout[26] = _or([Din[26], Din[25]])
	Dout[25] = _and([Din[26], _not(Din[25])])
	Dout[24] = _or([Din[24], _not(Din[23])])
	Dout[23] = _nor([Din[24], _not(Din[23])])
	Dout[22] = _nand([Din[24], _not(Din[23])])
	Dout[21] = _nor([Din[22], Din[21], Din[20]])
	Dout[20] = _and([Din[22], _not(Din[21]), _not(Din[20])])
	Dout[19] = _nand([Din[22], Din[21], _not(Din[20])])
	Dout[18] = _or([Din[19], Din[18], _not(Din[17])])
	Dout[17] = _nand([_not(Din[19]), _not(Din[18]), _not(Din[16])])
	Dout[16] = _nor([_not(Din[19]), _not(Din[18]), _not(Din[16])])
	Dout[15] = _and([_not(Din[15]), _not(Din[14])])
	Dout[14] = _nand([(Din[15]), _not(Din[14])])
	Dout[13] = _nor([(Din[15]), _not(Din[14])])
	Dout[12]  = _xor([Din[13], Din[12]])
	Dout[11]  = _xnor([Din[13], Din[12]])
	Dout[10] = _switch(Din[11], Din[10], Din[9])
	Dout[9] = _switch(_not(Din[9]), Din[11], Din[10])
	Dout[8] = _nand([Din[11], _not(Din[10]), _not(Din[9])])
	Dout[7] = _xor([Din[8], Din[7], Din[6]])
	Dout[6] = _nand([Din[8], Din[7], _not(Din[6])])
	Dout[5] = Din[4]
	Dout[4] = Din[3]
	Dout[3] = Din[5]
	Dout[2] = _not(Din[0])
	Dout[1] = _not(Din[2])
	Dout[0] = _not(Din[1])

stoptime = time.time()

outbits = "0b"
index = 31
for i in range(len(Dout)):
	outbits += "{}".format(Dout[index])
	index -= 1
	




