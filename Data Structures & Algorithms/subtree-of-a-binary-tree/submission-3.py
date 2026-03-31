class Solution:
    def treetolist(self, root):
        res = []
        stack = [root] 
        
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                res.append(None)
        return res

    def isSubtree(self, root, subRoot):
        main = self.treetolist(root)
        sub = self.treetolist(subRoot)
        
        for i in range(len(main) - len(sub) + 1):
            if main[i : i + len(sub)] == sub:
                return True
        return False