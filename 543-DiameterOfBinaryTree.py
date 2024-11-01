# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        leftDiameter = self.dfs(root.left)
        rightDiameter = self.dfs(root.right)

        self.max_diameter = max(self.max_diameter, leftDiameter + rightDiameter)

        return 1 + max(leftDiameter, rightDiameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter
