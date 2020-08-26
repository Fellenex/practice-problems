class LinkedList:

    def __init__(self, _seed):

        #add the first node supplied
            self.head = _seed
            self.tail = _seed

    def add(self, _node):
        self.tail.addNeighbour(_node)
        self.tail = _node


    def prettyPrint(self):
        curr = self.head
        prettyString = ''
        while curr:
            prettyString += str(curr.label) + ", "
            curr = curr.next
        #cut off the final comma
        prettyString = prettyString[:-2]
        print(prettyString)

    def getLength(self):
        x = self.head
        length = 1
        while not(x == self.tail):
            x = x.next
            length += 1
        return(length)


class Node:
    def __init__(self, _label):
        self.next = None
        self.label = _label

    def addNeighbour(self, _neighbourNode):
        self.next = _neighbourNode


#O(n^2) solution to reversing a linked list.
#Traverses the (shrinking) list starting from the head to find the last element yet to be added to the reversed list
def reverseLinkedList(_linkedList):
    if (_linkedList.head == _linkedList.tail) and (_linkedList.head.next is None):
        #list consists of only one element
        return(LinkedList(_linkedList.head))
    else:
        furthestIn = _linkedList.tail
        newLinkedList = LinkedList(Node(furthestIn.label))

        while not(_linkedList.head == furthestIn):

            #find the node that immediately precedes the node furthest into what we've seen
            newNext = _linkedList.head
            while not(newNext.next == furthestIn):
                newNext = newNext.next

            newLinkedList.add(Node(newNext.label))
            furthestIn = newNext

        return(newLinkedList)



linky = LinkedList(Node(0))
for x in range(1,10):
    linky.add(Node(x))
linky.prettyPrint()

revLinky = reverseLinkedList(linky)
revLinky.prettyPrint()
