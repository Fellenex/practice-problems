import random
import time
import sys

MAX_ARRAY_SIZE = 10
MAX_ROTATIONS = 5

#Moves the last element to the first position, numPushes times.
#O(n*k) time, such that k is a constant.
#
#Parameters:
#	_rotateMe: The array to be rotated
#	_numPushes: The number of times that the last element is pushed to the front
#
#Return Value:
#	_rotateMe: The array, rotated
#
def simple_rotate_array(_rotateMe, _numPushes):
	
	#Rotating a list of length 0 or 1 always yields the same list
	if (len(_rotateMe) == 0 or len(_rotateMe) == 1):#O(1)
		pass

	else:
		for i in range(_numPushes): 				#O(k)
			shift = _rotateMe[-1] 					#O(1)
			_rotateMe = [shift]+_rotateMe[:-1]		#O(n)

	return _rotateMe

#Switches the place of elements using a temporary variable
#O(n*k) time, such that k is a constant.
#
#Parameters:
#	_rotateMe: The array to be rotated
#	_numPushes: The number of times that the last element is pushed to the front
#
#Return Value:
#	_rotateMe: The array, rotated.
#
def space_saving_rotate_array(_rotateMe, _numPushes):
	
	#Rotating a list of length 0 or 1 always yields the same list.
	if (len(_rotateMe) == 0 or len(_rotateMe) == 1):#O(1)
		pass

	else:
		for i in range(_numPushes):					#O(k)
			head = _rotateMe[0]						#O(1)

			_rotateMe[0] = _rotateMe[-1]			#O(1)

			for j in range(1, len(_rotateMe)):		#O(n)
				temp = _rotateMe[j]					#O(1)
				_rotateMe[j] = head					#O(1)
				head = temp							#O(1)



	return _rotateMe


#Creates test data to be used in the array rotation problem
#Parameters:
#	_numTests: The number of test data.
#
#Return Value:
#	tests: A list of tuples of the form (<List of numbers>, <Number of rotations)
#
def generateTests(_numTests):
	tests = []
	for i in range(_numTests):
		tests.append( (range(random.randint(0,MAX_ARRAY_SIZE)), random.randint(0,MAX_ROTATIONS) ) )

	return tests


#Compares the time taken for the simple_rotate_array and the space_saving_rotate_array functions
#Parameters:
	#_numTests: The number of tests to use in each function
#Return Value:
	#None
def compareFunctions(_numTests):
	testsOne = generateTests(_numTests)
	testsTwo = testsOne[:]

	simpleTimes = []
	spaceSavingTimes = []

	simpleTotalStart = time.clock()
	for test in testsOne:
		simpleEachStart = time.clock()

		simple_rotate_array(test[0],test[1])

		simpleTimes.append(time.clock()-simpleEachStart)
	simpleTotalTime = time.clock()-simpleTotalStart

	spaceSavingTotalStart = time.clock()
	for test in testsTwo:
		spaceSavingEachStart = time.clock()

		space_saving_rotate_array(test[0],test[1])

		spaceSavingTimes.append(time.clock()-spaceSavingEachStart)
	spaceSavingTotalTime = time.clock()-spaceSavingTotalStart

	print "Simple Rotate Times:"
#	counter = 1
#	for s in simpleTimes:
#		if counter%5 == 0:
#			print str(s)
#		else:
#			sys.stdout.write(str(s)+'\t')
#
#		counter+=1
	print "Total Simple Rotate Time ("+str(_numTests)+" tests): "+str(simpleTotalTime)
	print "Average Simple Rotate Time ("+str(_numTests)+" tests): "+str(simpleTotalTime/_numTests)

	print

	print "Space Saving Rotate Times:"
#	counter = 1
#	for s in spaceSavingTimes:
#		if counter%5 == 0:
#			print str(s)
#		else:
#			sys.stdout.write(str(s)+'\t')

	print "Total Space Saving Rotate Time ("+str(_numTests)+" tests): "+str(spaceSavingTotalTime)
	print "Average Space Saving Rotate Time ("+str(_numTests)+" tests): "+str(spaceSavingTotalTime/_numTests)

	print "______________________"
	print


for i in range(1,11):
	compareFunctions(1000*i)