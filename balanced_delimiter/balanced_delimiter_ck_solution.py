#Checks for balanced delimiters.
#Written by Chris Keeler, August 18th 2015

DEBUG_MODE = False
ROUND = 0
SQUARE = 1
CURLY = 2

def debug(_message):
	if DEBUG_MODE:
		print _message

#Checks to see if a string contains balanced braces (, [, {, ), ], }
#Parameters:
#	_parseMe: A string, to be parsed.
#
#Return Value:
#	success: A boolean, representing whether the string is syntactically valid.
#
def balanced_delimiters(_parseMe):
	success = True
	
	mostRecent = []

	#We use a 3-digit string to represent what can be accepted
	counts = [0,0,0] #(round,square,curly)

	#States of acceptance:
	#	Can only accept open
	#	Can accept open or close

	#Digits ABC will represent [ (,[,{ ]
		#When it is 0, we can only accept opening braces, because we haven't yet opened one to close
		#When above 0, there are braces which need closing.

	#At the end of the parse, the number should be "000"
	#This verifies that there are the correct number of matching braces

	#Easy rejections
	if (len(_parseMe) % 2) != 0:
		success = False

	#Start parse
	for i in range(len(_parseMe)):

		#If we encounter an opening brace, then keep track of this brace which must eventually be closed.
		if _parseMe[i] == '(':
			counts[ROUND] += 1
			mostRecent.append('(')

		elif _parseMe[i] == '[':
			counts[SQUARE] += 1
			mostRecent.append('[')

		elif _parseMe[i] == '{':
			counts[CURLY] += 1
			mostRecent.append('{')

		else:

			#If we have a closing brace, then we must first have encountered an opening brace.
			#If we have one type of open brace and encounter a closing of another type, then they are unbalanced.
			#Successful closing means that we can pop off the most recent opening brace from the mostRecent stack.
			if _parseMe[i] == ')':
				if counts[ROUND] == 0:
					#Not accepting closing round brackets right now.
					debug("Not accepting closing round brackets right now.")
					success = False

				elif mostRecent[-1] != '(':
					#Round was not the most recent opening bracket.
					debug("Round was not the most recent opening bracket.")
					success = False

				else:
					counts[ROUND] -= 1
					mostRecent.pop()

			elif _parseMe[i] == ']':
				if counts[SQUARE] == 0:
					#Not accepting closing square brackets right now.
					debug("Not accepting closing square brackets right now.")
					success = False

				elif mostRecent[-1] != '[':
					#Square was not the most recent opening bracket.
					debug("Square was not the most recent opening bracket.")
					success = False

				else:
					counts[SQUARE] -= 1
					mostRecent.pop()

			elif _parseMe[i] == '}':
				if counts[CURLY] == 0:
					#Not accepting closing round brackets right now.
					debug("Not accepting closing curly brackets right now.")
					success = False

				elif mostRecent[-1] != '{':
					#Curly was not the most recent opening bracket.
					debug("Curly was not the most recent opening bracket.")
					success = False

				else:
					counts[CURLY] -= 1
					mostRecent.pop()

			else:
				#Invalid character.
				debug("Invalid character: "+_parseMe[i])
				success = False

	debug("Round count: "+str(counts[ROUND]))
	debug("Square count: "+str(counts[SQUARE]))
	debug("Curly count: "+str(counts[CURLY]))

	#If the delimiters aren't balanced, then
	if (counts[ROUND] != 0 or counts[SQUARE] != 0 or counts[CURLY] != 0):
		success = False

	return success

#Balanced delimiters.
print balanced_delimiters("[]")
print balanced_delimiters("()[]{}")
print balanced_delimiters("([{}])")
print balanced_delimiters("([]{})")


#Unbalanced delimiters
print balanced_delimiters("([)]")
print balanced_delimiters("([]")
print balanced_delimiters("[])")
print balanced_delimiters("([})")