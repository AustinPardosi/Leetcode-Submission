class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True

            return (1 + dfs(r+1, c) +
            dfs(r-1, c) +
            dfs(r, c+1) +
            dfs(r, c-1) )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    maxArea = max(maxArea, dfs(r, c))
                    
        return maxArea