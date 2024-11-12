# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], result: List[int]):
        if root == None:
            return result

        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result
