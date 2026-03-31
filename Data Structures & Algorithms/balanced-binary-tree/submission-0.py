class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            
            # If any subtree is unbalanced, bubble up a sentinel value (-1)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            
            return 1 + max(l, r)

        return dfs(root) != -1 # Check if sentinel value was ever triggered