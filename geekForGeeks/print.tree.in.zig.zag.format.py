# from .tree import Tree
from collections import deque


class Node(object):
    def __init__(self, val=None):
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


class PrintTreeInZigZagFormat(Tree):

    def printTreeInZigZageFormat(self):
        flag = True
        queue = deque()
        root = Tree.root
        queue.append(root)

        while queue:
            for q in range(len(queue)):
                if flag:
                    node = queue.pop()
                    print(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    node = queue.popleft()
                    print(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            flag = not flag


PrintTreeInZigZagFormat().printTreeInZigZageFormat()
