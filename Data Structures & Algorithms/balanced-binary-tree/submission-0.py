# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node):
        if(node==None):
            return (0, True)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        balanced = False
        if(abs(left[0]-right[0])<=1 and left[1] and right[1]):
            balanced = True
        return (1+max(left[0], right[0])), balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
        