class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def check_path(root,sequence,pathData, temp=[]):
    if root is None:
        return False
    temp.append(root.val)
    if temp == sequence and root.right is None and root.left is None:
        pathData.append(tuple(temp))
    check_path(root.left, sequence, pathData, temp)
    check_path(root.right, sequence, pathData, temp)
    temp.pop()

def find_path(root, sequence):
    pathData = []
    check_path(root, sequence,pathData)
    if pathData:
        return pathData[0] == tuple(sequence)
    return False


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()