class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        basically the idea is in order to minimize the number of intervals we need to remove,
        within a range of overlapping intervals, we should greedily merge them into the smallest merged interval. This way, we can fit more intervals within this range and hence we need to remove less. and once this merging is done, we find the difference in length of the merged intervals and original, and this is the minimum number we need to remove

        we merge by taking min(ends)

        to check if overlap, start_2 < end_1
        """

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        latest = sorted_intervals[0][1]
        length = 1

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < latest:
                latest = min(sorted_intervals[i][1], latest)
            else:
                length += 1
                latest = sorted_intervals[i][1]

        return len(sorted_intervals) - length 