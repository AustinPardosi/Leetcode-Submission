class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0 

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range (rows)]
        numOfIsland = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c >= cols or c < 0 or visited[r][c] or grid[r][c] == '0':
                return 
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited[r][c]:
                    numOfIsland += 1
                    dfs(r, c)
        
        return numOfIsland