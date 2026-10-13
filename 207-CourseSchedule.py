from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacencyList = defaultdict(list) # course -> [preq]
        # create the visited state array
        visited = [0] * numCourses # 0 - not visited, 1 - currently visited (potential cyclic), 2 - finished (safe visited)

        # build the adjacency list
        for data in prerequisites:
            course, preq = data[0], data[1]
            adjacencyList[course].append(preq)
        
        def dfs(course):
            if visited[course] == 1:
                return False # Cyclic
            if visited[course] == 2:
                return True # Safe

            # currently visiting
            visited[course] = 1

            # check the prereq if its has cycle (currently checked by others)
            for preq in adjacencyList[course]:
                if not dfs(preq):
                    return False
            
            # Done visiting
            visited[course] = 2 
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
