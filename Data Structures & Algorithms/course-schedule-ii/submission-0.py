from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #set up our adjacency list and indegree
        adjList = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range (numCourses)}

        for pair in prerequisites:
            course, prereq = pair

            adjList[prereq].append(course)
            indegree[course] += 1

        zero_nodes = deque([])
        #find nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_nodes.append(i)
        
        #keep processing courses with 0 prereqs left to check if we can finish everything
        processed = 0 
        sequence = []
        while zero_nodes:
            curr_course = zero_nodes.pop()
            sequence.append(curr_course)
            processed += 1

            for course in adjList[curr_course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    zero_nodes.append(course)


        if processed == numCourses:
            return sequence
        
        return []