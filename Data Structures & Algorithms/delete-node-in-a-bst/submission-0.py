class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
            return root
        
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.deleteNode(curr.left, key)
                    return root
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.deleteNode(curr.right, key)
                    return root
                curr = curr.right
        
        return root