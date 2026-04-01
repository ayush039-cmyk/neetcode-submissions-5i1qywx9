# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        res = []
        curr = root
        while stack:
            level = []
            for i in range(len(stack)):
                curr = stack.popleft()
                level.append(curr.val)
                stack.append(curr.left) if curr.left else None
                stack.append(curr.right) if curr.right else None
            res.append(level)
        return res
