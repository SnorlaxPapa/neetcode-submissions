class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def search(index, prefix, curr_sum):
            nonlocal nums
            nonlocal results

            if curr_sum > target:
                return
            
            if curr_sum == target:
                results.append(prefix[:])
                return
    
            for i in range(index, len(nums)):
                prefix.append(nums[i])
                curr_sum += nums[i]
                search(i, prefix, curr_sum)
                prefix.pop()
                curr_sum -= nums[i]
        
        nums = sorted(nums)
        search(0, [], 0)

        return results