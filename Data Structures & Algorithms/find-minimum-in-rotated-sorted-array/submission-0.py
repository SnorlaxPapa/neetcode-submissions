class Solution:
    def findMin(self, nums: List[int]) -> int:
        """trivial solution is a O(n) pass through
        so [3, 4, 5, 6, 1, 2] -> min 1
        However, question is asking for a logn run time. 
        a log n run time suggests splitting the array into 2 -> binary search
        but this array is unsorted, and any attempt at sorting will be > log n
        let us look at sample case
        3, 2 l and r bound. if we take the middle, e.g. 5. what can we tell from this?
        the original array is strictly increasing. 
        we can infer that the array has been rotated, and between the middle and r bound, it is increasing, then decreasing, and the minimum is somewhere between thsi bound
        so we should set left bound to middle + 1
        what if middle is smaller than r bound? that means that between the middle and right bound, it is increasing, and the array has not been rotated to that degree yet
        so we should set r bound to middle - 1
        if middle > r bound, set r as min, search right
        if middle < r bound, set middle as min, search left (no need equals as no unique)
        return min
        logn run time
        """

        left = 0
        right = len(nums) - 1
        minElement = nums[0]

        while left <= right:
            middle = (left + right)//2
            if nums[middle] > nums[right]:
                minElement = min(minElement, nums[right])
                left = middle + 1
            else: 
                minElement = min(minElement, nums[middle])
                right = middle - 1
        return minElement