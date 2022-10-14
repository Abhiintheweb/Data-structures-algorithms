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

'''
            10
            / \
        12     13       
        / \    / \
      14    15 16 17
'''

# if __name__ == '__main__':
