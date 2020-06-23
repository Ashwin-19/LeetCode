# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        
        self.elements = set()
        self.recover(root, 0, "root")
        
    
    def recover(self, root, parent, side):
        
        if root != None:
            if side == 'root':
                root.val = 0        
            if side == 'l':
                root.val = 2*parent + 1
            if side == 'r':
                root.val = 2*parent + 2
            
            self.elements.add(root.val)
            self.recover(root.left,root.val,'l')
            self.recover(root.right,root.val,'r')
        else:
            return
        

    def find(self, target: int) -> bool:
        
        if target in self.elements:
            return True
        else:
            return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)