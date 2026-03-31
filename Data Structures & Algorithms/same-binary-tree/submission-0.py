# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btolist(self,root):
        stack = []
        res = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                res.append(None)
                curr = stack.pop()
        return res

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ptolist = self.btolist(p)
        qtolist = self.btolist(q)

        if ptolist != qtolist:
            return False
        for i in range(max(len(ptolist),len(qtolist))):
            if ptolist[i] != qtolist[i]:
                return False
        return True