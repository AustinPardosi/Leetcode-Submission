class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # Instead of checking this cell could go to teh ocean or not, better just list all the possible cell than can be reached from the ocean
        result = []
        row, col = len(heights), len(heights[0])
        movements = [(0,1), (0,-1), (1,0), (-1,0)]
        pacific = set()
        atlantic = set()

        # Logic of the flowing water
        def dfs(r, c, ocean):
            # Store the cell into the possible cell
            ocean.add((r, c))

            for dr,dc in movements:
                currR, currC = r+dr, c+dc

                if (0 <= currR < row and
                    0 <= currC < col and
                    (currR, currC) not in ocean and
                    heights[currR][currC] >= heights[r][c]):
                    dfs(currR, currC, ocean)
        
        # Do the dfs from the ocean
        # Pacific = top & left most
        for c in range(col):
            dfs(0, c, pacific)
        for r in range(row):
            dfs(r, 0, pacific)

        # Atlantic = bottom & right most
        for c in range(col):
            dfs(row-1, c, atlantic)
        for r in range(row):
            dfs(r, col-1, atlantic)
        
        # List all the cell that goes to both ocean
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result