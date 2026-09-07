from collections import defaultdict
class Solution: 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dataRow = defaultdict(set) # row -> set of values
        dataCol = defaultdict(set) # col -> set of values
        dataBox = defaultdict(set) # box -> set of values

        for i, rowVal in enumerate(board):
            for j, val in enumerate(rowVal):
                if val == ".":
                    continue

                box = (i//3, j//3)

                if val in dataRow[i] or val in dataCol[j] or val in dataBox[box]:
                    return False

                dataRow[i].add(val)
                dataCol[j].add(val)
                dataBox[box].add(val)

        return True

# better on runtime cause set and better memory too
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, rowVal in enumerate(board):
            for j, val in enumerate(rowVal):
                if val == ".":
                    continue

                box = (i//3, j//3)
                if ('r', i, val) in seen or ('c', j, val) in seen or ('b', box, val) in seen:
                    return False

                seen.add(('r', i, val))
                seen.add(('c', j, val))
                seen.add(('b', box, val))

        return True