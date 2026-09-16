from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        end result looks like a graph
        we can create an adjacency list pointing to prereq courses
         
        our number of courses cannot be finished if we have one course serving as a prerequisite for another course
        but the prerequisite of this course is our original course

        so we can see this forms a cycle in a graph

        are there any other conditions for our number of courses to not be satisfied?

        len(prerequisite) > numcourses? possible for one course to have numerous prereqs
        len(prerequisite) < numcourses? some courses don't have prereqs maybe

        courses can share prereqs as well

        craft an adjacency list for all the classes.
        
        the adjacency list includes all nodes with a prerequisite
        we use a topological sort to check for the cycle with kahn's

        we append all nodes to a queue and process until queue is empty
        once process exits, if length of queue same as numcourses, we've covered all courses
        if not means there is a cycle and cannot complete
        """

        adj_list = {i: set() for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        #create adjacency tree prerequisite -> courses that depend on it
        for node, prereq in prerequisites:
            adj_list[prereq].add(node)

        #create indegree hashmap
        for prereq, dependants in adj_list.items():
            for dependant in dependants:
                indegree[dependant] = indegree.get(dependant, 0) +  1

        #get 0 indegree first
        queue = deque([])
        for node, count in indegree.items():
            if count == 0:
                queue.append(node)

        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1

            for dependant in adj_list[node]:
                indegree[dependant] -= 1
                if indegree[dependant] == 0:
                    queue.append(dependant)

        if processed == numCourses: return True
        return False


