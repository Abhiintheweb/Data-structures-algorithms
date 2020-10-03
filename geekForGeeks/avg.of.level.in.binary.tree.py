from collections import deque;
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
    result = []
    q = deque()
    q.append(root)
    while q:
        temp = []
        for _ in range(len(q)):
            node = q.pop()
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
            temp.append(node.val)
        result.append(sum(temp)/len(temp))
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))
main()


