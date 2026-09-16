class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_max, current_min = 1, 1
        global_max = nums[0]

        for i in range(0, len(nums)):
            if nums[i] == 0:
                global_max = max(global_max, 0)
                current_max, current_min = 1, 1
                continue
            if nums[i] > 0:
                current_max *= nums[i]
                current_min *= nums[i]

            if nums[i] < 0:
                current_min *= nums[i]
                current_max *= nums[i]

                if current_min > 0:
                    tmp = current_max
                    current_max = current_min
                    current_min = tmp
                else:
                    current_max = nums[i]

            global_max = max(global_max, current_max)
            current_max = max(1, current_max)


        return global_max
            

