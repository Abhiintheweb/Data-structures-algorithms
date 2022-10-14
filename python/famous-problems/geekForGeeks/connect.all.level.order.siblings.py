from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    previousLevel = None
    while queue:
        previousNode = None
        levelSize = len(queue)
        for i in range(levelSize):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if previousNode:
                previousNode.next = node
            previousNode = node

            if i ==0 and previousLevel:
                previousLevel.next = node
            if i == levelSize-1:
                previousLevel = node


def connect_all_siblings2(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    currentNode, previousNode  = None , None
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            if previousNode and currentNode:
                previousNode.next = currentNode
            previousNode = currentNode




def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()
  connect_all_siblings2(root)
  root.print_tree()


main()
