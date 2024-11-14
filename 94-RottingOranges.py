class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for i, j in directions:
                    nRow, nCol = i + r, j + c
                    if (nRow < 0 or nRow >= rows or nCol < 0 or nCol >= cols or grid[nRow][nCol] != 1 ):
                        continue
                    grid[nRow][nCol] = 2
                    fresh -= 1
                    q.append([nRow, nCol])
            time += 1

        if fresh > 0 :
            return -1
        else:
            return time

