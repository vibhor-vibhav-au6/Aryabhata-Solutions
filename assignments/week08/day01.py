# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root):
        if root :
            self.helper(root.left)
            self.soln.append(root.val)
            self.helper(root.right)
        return self.soln
    
    
    def kthSmallest(self, root, k):
        self.soln = []
        self.helper(root)
        return self.soln[k-1]