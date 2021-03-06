class BinaryTree():
    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())



if __name__ == "__main__":
    myTree = BinaryTree("Duddy")
    myTree.insertLeft("Pan")
    myTree.insertRight("Marianne")
    myTree.insertRight("Chow")
    myTree.insertLeft("Michelle")
    myTree.insertLeft("Maybelle")
    myTree.insertLeft("Melody")
    myTree.setNodeValue("MaPa")

    print myTree.getNodeValue()
    printTree(myTree)