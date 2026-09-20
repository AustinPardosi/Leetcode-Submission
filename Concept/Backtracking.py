# def subsets(nuts):
# 	answer =  []
# 	path = []

# 	def backtracking(start):
# 		# If Condition
# 		answer.append(path.copy())		

# 		# For every choices
# 		for i in range (start, len(nuts)):
# 			# Make choices
# 			path.append(nuts[i])
# 			# Explore
# 			backtracking(i+1)
			
# 			# Undo Choices
# 			path.pop()
	
# 	backtracking(0)
# 	return answer

# print(subsets([1,2,3]))

# def combinations(nums, k):
#     answer = []
#     path = []

#     def backtracking(start, k):
#         # If condition
#         if len(path) == k:
#             answer.append(path.copy())
#             return

#         # For every choices
#         for i in range(start, len(nums)):
#             # Make Choises
#             path.append(nums[i])
            
#             # Explore
#             backtracking(i+1, k)

#             # Undo Choices
#             path.pop()

#     backtracking(0, k)
#     return answer

# print(combinations([1,2,3,4], 2))


# def permutation(nums):
#     answer = []
#     path = []
#     used = [False] * len(nums)

#     def backtracking():
#         # If condition
#         if len(path) == len(nums):
#             answer.append(path.copy())
#             return

#         # For every choices
#         for i in range(len(nums)):
#             # Make choices
#             # If its already used, skip it
#             if used[i]:
#                 continue
#             path.append(nums[i])
#             used[i] = True

#             # Explore
#             backtracking()

#             # Undo Choices
#             used[i] = False
#             path.pop()

#     backtracking()
#     return answer

# print(permutation([1,2,3]))

def maze(grid):
    row = len(grid)
    col = len(grid[0])

    visited = set()
    path = []
    answer = []

    def dfs(r, c):
        # If condition
        if (r < 0 or r >= row or
            c < 0 or c >= col or
            grid[r][c] == "#" or
            (r, c) in visited):
            return False

        # For every choices 
        visited.add((r,c))
        path.append((r,c))

        if grid[r][c] == "E":
            answer.append(path.copy())
            return True

        movement = [(0,1), (0,-1), (1,0), (-1,0)]

        # Explore
        for dr, dc in movement:
            if dfs(r+dr, c+dc):
                return True


        # Undo Choices
        path.pop()

        return False

    return dfs(0, 0), answer

print(maze([
    ["S", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", "."],
    [".", ".", "#", "#", ".", ".", "."],
    ["#", ".", "#", "E", ".", "#", "."]
]))

