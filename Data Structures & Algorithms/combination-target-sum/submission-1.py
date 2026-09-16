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
                if curr_sum + nums[i] > target:
                    break  
                prefix.append(nums[i])
                search(i, prefix, curr_sum + nums[i])
                prefix.pop()
        
        nums = sorted(nums)
        search(0, [], 0)

        return results