# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return ",#"  # Unique marker for null pointers
            
            # Pre-order: Root -> Left -> Right
            # Notice the leading comma ',' delimiter: it prevents partial number matches (e.g., '12' vs '2')
            return f",{node.val}" + serialize(node.left) + serialize(node.right)
        
        full_tree = serialize(root)
        sub_tree = serialize(subRoot)
        
        # Substring check: O(N + M) average time in Python
        return sub_tree in full_tree