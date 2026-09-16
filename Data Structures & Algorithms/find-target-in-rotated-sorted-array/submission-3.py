class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        we should search for the pivot point first, before searching for the target in the segment we expect to find it in
        e.g. 4 5 6 7 0 1 2 target 6
        pivot point = 0
        is target <= arr[-1]? if yes, its in the right segment. otherwise it's in the left segment
        
        to find pivot, check if middle > right, if yes, then pivot point is to the right
        if no, then pivot point is to the left
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left+right)//2

            if nums[middle] > nums[right]:
                left = middle + 1
            else: #middle less than right, close right space
                right = middle

        if target <= nums[-1]:
            right = len(nums) - 1
        else:
            right = left - 1
            left = 0

        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target: return middle
            elif nums[middle] > target: right = middle - 1
            else: left = middle + 1

        return -1   