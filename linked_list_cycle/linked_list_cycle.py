import random

class Node():
	def __init__(self, _value, _next=None):
		self.value = _value
		self.next = _next

class LoopNode(Node):
	def __init__(self, _value, _next=None):
		self.value = _value
		self.next = _next
		self.visited = False


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


def generate_unlooped_linked_list(_listSize):
	head = LoopNode(random.randint(1,100))
	tempOne = head
	for i in range(_listSize-1):
		tempTwo = LoopNode(random.randint(1,100))
		tempOne.next = tempTwo
		tempOne = tempTwo

	return head

def generate_looped_linked_list(_listSize):
	head = LoopNode(random.randint(1,100))
	tempOne = head
	for i in range(_listSize-1):
		tempTwo = LoopNode(random.randint(1,100))
		tempOne.next = tempTwo
		tempOne = tempTwo

	return head

#Return Value:
#
#
def detectLoop(_activeItem):
	if _activeItem.next == None:
		#The end of the list! No loop was found.
		return False
	else:
		if _activeItem.visited:
			#This node has already been visited!
			#This is the start of our loop.
			return defineLoop(_activeItem)
		else:
			_activeItem.visited = True
			return detectLoop(_activeItem.next)



def defineLoop(_loopHead):
	print "oh look we found one"
	loop = [_loopHead]
	active = _loopHead
	while active.next != _loopHead:
		loop.append(active.next)
		active = active.next

	return loop



h = generate_linked_list(5)

#while h.next != None:
#	print "V: "+str(h.value)
#	h = h.next

print detectLoop(h)


head = LoopNode(1)
two = LoopNode(2)
three = LoopNode(3)
four = LoopNode(4)
five = LoopNode(5)  

head.next = two
two.next = three
three.next = four
four.next = five
five.next = five

foundLoop = detectLoop(head)

for i in foundLoop:
	print i.value