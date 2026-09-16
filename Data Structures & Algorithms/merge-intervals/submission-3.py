class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort by starting time, then merge 
        arrays are in order such that start_2 >= start_1

        end_2 >= end_1 or end_2 < end_1

        overlapping occurs when start_2 <= end_1
        we merge by taking min(start_1, start_2), max(end_1, end_2)

        use a stack so we can merge lol
        """

        results = []
        sort_intervals = sorted(intervals, key = lambda x: x[0])
        n = len(intervals)

        i = 0
        while i < n:
            results.append(sort_intervals[i])
            #keep merging until no more overlap
            while i < n-1 and results[-1][1] >= sort_intervals[i+1][0]:
                results[-1] = [results[-1][0], max(results[-1][1], sort_intervals[i+1][1])]
                i += 1
            
            i += 1


        return results

            
            

