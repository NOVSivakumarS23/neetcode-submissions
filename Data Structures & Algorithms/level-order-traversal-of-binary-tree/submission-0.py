# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root==None:
            return result
        queue = deque([root])

        while(len(queue) != 0):
            size = len(queue)
            arr = []
            for i in range(size):
                arr.append(queue[0].val)
                if(queue[0].left!=None): queue.append(queue[0].left)
                if(queue[0].right!=None): queue.append(queue[0].right)
                queue.popleft()
            result.append(arr)
        return result