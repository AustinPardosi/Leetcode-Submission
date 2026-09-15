# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isInRange(node, low, high):
            if node is None:
                return True

            if  node.val >= high or node.val <= low:
                return False
            
            left = isInRange(node.left, low, min(node.val, high))
            right = isInRange(node.right, max(node.val, low), high)
            return left and right
        
        return isInRange(root, -math.inf, math.inf)