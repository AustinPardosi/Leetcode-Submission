class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        movement = [(0,1), (0,-1), (1,0), (-1,0)]
        target = list(word)

        def dfs(r, c, i):
            # Invalid
            if (r < 0 or r >= row or
                c < 0 or c >= col or
                (r,c) in visited):
                return False
            
            # Character doesnt match
            if (board[r][c] != target[i]):
                return False
            
            # We find all of the word
            if (i == len(target)-1):
                return True
            
            # Choose
            visited.add((r,c))

            # Explore
            for dr, dc in movement:
                if (dfs(r+dr, c+dc, i+1)):
                    return True
            
            # Undo
            visited.remove((r,c))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (dfs(i, j, 0)):
                    return True
        return False
