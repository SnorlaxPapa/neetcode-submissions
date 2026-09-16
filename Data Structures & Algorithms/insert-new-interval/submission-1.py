class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]
        result = []
        new_start, new_end = newInterval
        n = len(intervals)

        idx = 0
        while idx < n and intervals[idx][1] < new_start:
            result.append(intervals[idx])
            idx += 1
        
    
        merged_interval = newInterval
        while idx < n and intervals[idx][0] <= new_end:
            merged_interval = [min(merged_interval[0], intervals[idx][0]), max(merged_interval[1], intervals[idx][1])]
            idx += 1
        
        result.append(merged_interval)

        while idx < n:
            result.append(intervals[idx])
            idx += 1

        return result

