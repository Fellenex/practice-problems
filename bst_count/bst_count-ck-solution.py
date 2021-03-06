

class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def addChild(self, value):
        #adds to the left if this is the first child, otherwise adds to the right child.
        if not(self.leftChild):
            self.leftChild = Node(value)
        elif not(self.rightChild):
            self.rightChild = Node(value)
        else:
            print("Cannot add %s as a child to node %s" % (value, self.value))

    def isLeaf(self):
        return(not(self.leftChild) and not(self.rightChild))

    def __str__(self):
        return(str(self.value))

    def nodeCount(self):
        count = 1
        if self.leftChild: count += self.leftChild.nodeCount()
        if self.rightChild: count += self.rightChild.nodeCount()

        return(count)

    def descendantsCount(self):
        leftHeight = 0
        rightHeight = 0
        if self.leftChild: leftHeight = self.leftChild.descendantsCount()
        if self.rightChild: rightHeight= self.rightChild.descendantsCount()
        return 1 + max(leftHeight, rightHeight)


class Tree:
    def __init__(self, root):
        self.root = root

    def nodeCount(self):
        if self.root: return(self.root.nodeCount())
        else: return(0)

    def height(self):
        # -1 because the problem asks for the "depth reached", not the total number of levels in the tree.
        if self.root: return(self.root.descendantsCount() - 1)
        else: return(0)

    def __str__(self):
        return(str(self.root) + str(self.root.leftChild) + str(self.root.rightChild))


root = Node(0)
tree = Tree(root)
tree.root.addChild(1)
tree.root.addChild(2)
tree.root.leftChild.addChild(3)
tree.root.leftChild.addChild(4)
tree.root.rightChild.addChild(5)
tree.root.rightChild.addChild(6)

print(tree.nodeCount())
print(tree.height())


root = Node(0)
t2 = Tree(root)

t3 = Tree(None)
print(t3.nodeCount())
print(t3.height())
