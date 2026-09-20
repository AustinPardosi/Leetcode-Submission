class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []
        candidates.sort()

        def backtracking(start, target):
            # If Condition
            if target == 0:
                result.append(path.copy())
                return

            # For every choices
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                # Make Choises
                path.append(candidates[i])

                # Explore
                backtracking(i, target-candidates[i])

                # Undo Choises
                path.pop()
        
        backtracking(0, target)
        return result