class TreeNode:
    def __init__( self, val, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers( root ):
    allPaths = []
    paths = find_sum_path_recursive(root, allPaths, '')
    sum = 0
    for path in allPaths:
        sum += int(path)
    return sum


def find_sum_path_recursive( root, allPaths, path ):
    if root is None:
        return ''

    path += str(root.val)

    if root.left is None and root.right is None:
        allPaths.append(path)
    else:
        find_sum_path_recursive(root.left, allPaths, path)
        find_sum_path_recursive(root.right, allPaths, path)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
