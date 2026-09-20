    #                 GRAPH
    #                   │
    #       ┌───────────┴───────────┐
    #       │                       │
    #  Adjacency List            Matrix
    #    (Graph)
    #       │                       │
    #   ┌───┴───┐               ┌───┴───┐
    #   │       │               │       │
    #  DFS     BFS             DFS     BFS
    #   │       │               │       │
    # stack    queue          recursion queue

# Adjacency List
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A"],
#     "D": ["B"]
# }

## Graph DFS
# visited = set()

# def dfs(node):
#     if node in visited:
#         return

#     visited.add(node)

#     for neighbour in graph[node]:
#         dfs(neighbour)
 

## Graph BFS
# from collections import deque

# visited = set()
# queue = deque([start])

# while queue:
#     node = queue.popleft()

#     if node in visited:
#         continue

#     visited.add(node)

#     for neighbour in graph[node]:
#         queue.append(neighbour)

## Matrix directions
# directions = [
#     (-1, 0),
#     (1, 0),
#     (0, -1),
#     (0, 1)
# ]


## Matrix DFS
# def dfs(r,c):
#     if invalid:
#         return

#     mark_visited()

#     for dr, dc in directions:
#         dfs(r+dr, c+dc)


## Matrix BFS
# queue = deque([(r,c)])
# mark_visited()

# while queue:
#     node = queue.popleft()

#     for dr, dc in directions:
#         ...