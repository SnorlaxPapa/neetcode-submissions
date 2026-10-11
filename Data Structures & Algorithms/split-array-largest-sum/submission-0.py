class Solution:
    def checkArrays(self, nums, limit):
        num_arrays = 1
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum > limit:
                curr_sum = num
                num_arrays += 1
        
        return num_arrays

    def splitArray(self, nums: List[int], k: int) -> int:
        """
         we binary search the largest possible sum

        so our upper limit is the sum of the array 
        and the lower limit can be set to the max of the array (to reduce search space)
        then we check the middle, given this maximum subarray sum, how many subarrays do we need to fit within the maximum subarray sum

        if its more than k, we need to increase the subarray sum
        if its less than or equals to k, we can decrease the sum. also, we can set this to our candidate, because if it is the minimized subarray sum, we are guaranteed that we can fit k subarrays. if it is so large that we need less than k subarrays, decreasing the sum ensures that we will have k subarrays
        """
        
        psum = [0]
        max_num = float("-inf")
        right = 0

        for num in nums:
            max_num = max(max_num, num)
            right += num

        left = max_num
        res = 0
        while (left <= right):
            middle = left + (right - left) // 2

            subarrays_needed = self.checkArrays(nums, middle)
            
            if subarrays_needed <= k:
                res = middle
                right = middle - 1
            
            else:
                left = middle + 1

        return res

        

        

        



