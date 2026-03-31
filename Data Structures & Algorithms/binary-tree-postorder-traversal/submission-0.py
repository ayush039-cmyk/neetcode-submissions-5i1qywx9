# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp == None:
                    temp = stack[-1]
                    stack.pop()
                    res.append(temp.val)
                    while stack and temp == stack[-1].right:
                     temp = stack[-1]
                     stack.pop()
                     res.append(temp.val)
                else:
                    curr = temp
        return res