class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Hash map for O(1) index lookups in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        pre_idx = 0  # Global pointer to move sequentially through preorder

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            # Base case: no elements to construct subtree
            if in_left > in_right:
                return None

            # Pick current root value from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1  # Move to next root element for subtrees

            # Split point in inorder array
            index = inorder_map[root_val]

            # Build left and right subtrees recursively
            # NOTE: MUST build left subtree first because preorder goes Root -> Left -> Right
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)