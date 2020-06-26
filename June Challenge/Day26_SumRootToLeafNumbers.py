# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        return self.getsum(root,digits='')
    
    
    def getsum(self, root, digits):
        
        if root != None:
            
            digits += str(root.val)
            
            if root.left == None and root.right == None:
                
                return int(digits)
            
            else:
                
                return self.getsum(root.left,digits) + self.getsum(root.right,digits)
        
        return 0