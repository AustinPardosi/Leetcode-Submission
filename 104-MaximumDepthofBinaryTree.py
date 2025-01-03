# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth, leftVal, rightVal = 0, 0, 0

        if root == None:
            return 0

        leftVal += self.maxDepth(root.left)
        rightVal += self.maxDepth(root.right)

        return 1 + max(leftVal, rightVal)
    
# BFS Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 0

        if root == None:
            return 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            level += 1
        return level
