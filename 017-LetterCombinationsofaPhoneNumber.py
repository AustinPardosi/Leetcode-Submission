class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        data = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        def backtracking(index, current):
            # We have chosen one letter for every digit
            if index == len(digits):
                result.append(current)
                return
            
            # Try every possible letter for this digit
            for possible in (data[digits[index]]):
                backtracking(index + 1, current + possible)
        
        backtracking(0, "")

        return result