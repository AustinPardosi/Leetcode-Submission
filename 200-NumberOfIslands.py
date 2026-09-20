class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        movement = [(0,1), (0,-1), (1,0), (-1,0)]
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            # Check invalid
            if (r<0 or r>=row or
                c<0 or c>=col or
                grid[r][c] == "0"):
                return

            # Change island into water
            grid[r][c] = "0"

            # Change every island adjacent to it into water
            for dr, dc in movement:
                dfs(r+dr, c+dc)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    # found a island
                    count += 1
                    # destroy island into water
                    dfs(i, j)

        return count