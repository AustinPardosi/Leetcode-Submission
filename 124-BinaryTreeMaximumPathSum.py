# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, maxSum):
            if node is None:
                return 0, maxSum

            left, maxSum = dfs(node.left, maxSum)
            right, maxSum = dfs(node.right, maxSum)

            left = max(0, left)
            right = max(0, right)

            currVal = left + node.val + right

            maxSum = max(currVal, maxSum)
            path = node.val + max(left, right)
            return path, maxSum
        
        path, bigSum =  dfs(root, -math.inf)
        return bigSum