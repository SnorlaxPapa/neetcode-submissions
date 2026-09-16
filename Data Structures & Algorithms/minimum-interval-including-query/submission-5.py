import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        sort queries in ascending order
        sort intervals by interval length

        we create a set of queries for easy lookup = (index, queries)
        """
        query_index = [(query, idx) for idx, query in enumerate(queries)]
        query_index.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: x[0])
        results = [-1 for _ in range(len(queries))]

        min_distance = []
        i = 0

        for query, idx in query_index:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(min_distance, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while min_distance and min_distance[0][1] < query:
                heapq.heappop(min_distance)
            
            if min_distance:
                results[idx] = min_distance[0][0]
        
        return results
