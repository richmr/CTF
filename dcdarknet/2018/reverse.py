# segmented brute force reverser

import simpleob_mod as so
from logic import _nand, _not

def nextBits(currentBits):
	# Progresses a bit array
	# returns false if the array overflows current length
	currlen = len(currentBits)
	val = so.convertBitArrayToInt(currentBits)
	val = val + 1
	if (len(bin(val)[2:]) > currlen):
		return False
		
	return so.convertIntToBitArray(val, currlen)

def segBruteForce(bitGroups, goal):
	# bit Group is an array of bit groupings
	# bit groupings describe which in bits affect which out bits
	# for instance [[28, 27], [28, 27]] means in bits 28 and 27 effect out bits 28 and 27
	# or [[19, 18, 17, 16], [18, 17, 16]] means bits 19-16 effect out bits 18-16	
	# goal contains the answer we are looking for
	
	solved = [0 for i in range(len(goal))]
	solution = [0 for i in range(len(goal))]
	
	for aGroup in bitGroups:
		index = aGroup[0]
		outdex = aGroup[1]
		
		# init the in array
		inarray = [0 for i in range(len(index))]
		
		# grab the answer slice
		outgoal = [goal[i] for i in outdex]
		
		while (inarray):
			in_attempt = solution
			for i in range(len(inarray)):
				in_attempt[index[i]] = inarray[i] 
			out_attempt = so.run(in_attempt)
			out_slice = [out_attempt[i] for i in outdex]
			if (out_slice == outgoal):
				solution = in_attempt
				for i in range(len(index)):
					solved[index[i]] = 1
				break
			inarray = nextBits(inarray)
			
	if (_nand(solved)):
		for i in range(len(solved)):
			if (_not(solved[i])):
				print "[!] No solution found for bit {}".format(i)
	else:
		print "[+] Full solution found"
	
	print "[+] Solution found: {}".format(hex(so.convertBitArrayToInt(solution)))
	
bitGroups = []
bitGroups.append([[30], [31]])
bitGroups.append([[31], [30]])
bitGroups.append([[29], [29]])
bitGroups.append([[28, 27], [28,27]])
bitGroups.append([[26, 25], [26,25]])
bitGroups.append([[24, 23], [24,23,22]])
bitGroups.append([[22, 21,20], [21,20,19]])
bitGroups.append([[19, 18,17,16], [18,17,16]])
bitGroups.append([[15, 14], [15,14,13]])
bitGroups.append([[13, 12], [12,11]])
bitGroups.append([[11, 10,9], [10, 9, 8]])
bitGroups.append([[8, 7,6], [7,6]])
bitGroups.append([[4], [5]])
bitGroups.append([[3], [4]])
bitGroups.append([[5], [3]])
bitGroups.append([[0], [2]])
bitGroups.append([[2], [1]])
bitGroups.append([[1], [0]])

goal = 0xAF2A7613
goalArray = so.convertIntToBitArray(goal)

segBruteForce(bitGroups, goalArray)



	
	
			 
		