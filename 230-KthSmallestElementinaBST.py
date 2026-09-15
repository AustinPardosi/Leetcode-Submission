# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, k, count):
            if node is None:
                return None, count
            
            # Find Left
            result, count = dfs(node.left, k, count)
            if result is not None:
                return result, count
            
            # Val
            count += 1
            if count == k:
                return node.val, count

            # Find Right
            return dfs(node.right, k, count)
        
        result, _ = dfs(root, k, 0)
        return result