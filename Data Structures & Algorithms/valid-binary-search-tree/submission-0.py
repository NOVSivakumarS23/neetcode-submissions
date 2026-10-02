# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, small, big, cur) -> bool:
        if cur==None: return True
        if not (cur.val>small and cur.val<big):
            return False
        return self.dfs(small, cur.val, cur.left) and self.dfs(cur.val, big, cur.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float('-inf'), float('inf'), root)