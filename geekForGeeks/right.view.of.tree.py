from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__( self, val ):
        self.val = val
        self.left, self.right = None, None


def tree_right_view( root ):
    result = []
    q = deque()
    q.append(root)
    while q:
        queLen = len(q)
        for _ in range(queLen):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(node)


    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
