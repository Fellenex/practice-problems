from operator import xor

#Create a bitvector filled with False values
#
#Parameters:
#	_searchMe: The list of integers to be searched in the coupled ints problem
#				The largest integer in the list is used to determine the bitvector
#
#Return Value:
#	bitVector: A list of Falses, of length max(_searchMe)
#
def generate_bitVector(_searchMe):
	bitVector = [False]*max(_searchMe)
	return bitVector


#Loop through a list of integers to discover which are uncoupled.
#Parameters:
#	_searchMe: The list of integers to be searched
#	_bitVector: A bitvector to keep track of even/odd integer frequencies.
#
#Return Value:
#	None
#
def find_uncoupled_int(_searchMe,_bitVector):
	
	#Examine each integer, marking the bitvector in the index of the integer examined.
	#If we have yet to find the active integer, then 0 XOR 1 is 1
	#If we have already found one of the active integer, then 1 XOR 1 is 0.
	#By the end, all indices with a 1 are not in a couple.
	for item in _searchMe:
		print "i"+str(item)
		_bitVector[item-1] = xor(bool(_bitVector[item-1]), True)

	for v in range(len(_bitVector)):
		if _bitVector[v]:
			print str(v+1)+" doesn't belong to a couple."


myList = [1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5]
bv = generate_bitVector(myList)
find_uncoupled_int(myList,bv)