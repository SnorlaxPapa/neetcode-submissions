class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        def search(index, prefix):
            results.append(prefix[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue    

                prefix.append(nums[i])
                search(i+1, prefix)
                prefix.pop()

        search(0, [])

        return results