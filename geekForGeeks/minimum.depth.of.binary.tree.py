from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root,min_so_far=0):
    if not root:
        return  min_so_far
    return find_minimum_depth(root.left,min_so_far+1)
    return find_minimum_depth(root.right, min_so_far + 1)

def find_maximum_depth(root,max_so_far=0):
    q = deque()
    q.append(root)
    while q:
        max_so_far +=1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return max_so_far


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  print("Tree Max Depth: " + str(find_maximum_depth(root)))



main()
