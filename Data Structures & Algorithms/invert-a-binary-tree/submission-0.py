# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp

        print("Tree:")
        self.printTree(root)
        return root
    
    def printTree(self, root, level=0):
        if root:
            # Print the right subtree first (so it appears at the top)
            self.printTree(root.right, level + 1)
            
            # Print the current node with indentation
            print('    ' * level + '-> ' + str(root.val))
            
            # Print the left subtree
            self.printTree(root.left, level + 1)
