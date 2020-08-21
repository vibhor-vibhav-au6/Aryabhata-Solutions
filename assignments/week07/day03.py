# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    soln = []
    def helper(self, root):
        if root :
            self.soln.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
        return self.soln
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.soln = []
        self.helper(root)
        return self.soln

# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    soln = []
    def helper(self, root):
        if root :
            self.helper(root.left)
            self.helper(root.right)
            self.soln.append(root.val)            
        return self.soln
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.soln = []
        self.helper(root)
        return self.soln

# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    soln = []
    def helper(self, root):
        if root :
            self.helper(root.left)
            self.soln.append(root.val)
            self.helper(root.right)
        return self.soln
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.soln = []
        self.helper(root)
        return self.soln