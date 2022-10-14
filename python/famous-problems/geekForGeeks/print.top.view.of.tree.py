from collections import deque


class Node(object):
    def __init__( self, val=None ):
        self.left = None
        self.right = None
        self.val = val


class Tree(object):
    root = Node(10)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(14)
    root.left.right = Node(15)
    root.right.left = Node(16)
    root.right.right = Node(17)


class PrintTopViewOfTree(Tree):
    # @staticmethod
    def printTopViewOfTree(self, node, current=0, lastPrinted=0):
        if node:
            if current==0 and lastPrinted==0:
                print(node.val)
            elif current > lastPrinted:
                lastPrinted = current
                print(node.val)
            self.printTopViewOfTree(node.left,current+1, lastPrinted)
            self.printTopViewOfTree(node.right, current + 1, lastPrinted)

    def view(self):
        root = Tree.root
        self.printTopViewOfTree(root)

PrintTopViewOfTree().view()