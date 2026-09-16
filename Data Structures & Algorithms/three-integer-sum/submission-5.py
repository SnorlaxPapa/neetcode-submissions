class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        two sum avoiding current position. possibility that there may be more than one solution. so we make a list
        """
        left = 0
        right = len(nums) - 1
        answers = []
        while left < right:
            if nums[left] + nums[right] == target:
                answers.append(sorted([0-target, nums[left], nums[right]]))
                left+=1
                right-=1
            elif nums[left] + nums[right] > target:
                right-=1
            else:
                left+=1

        return answers


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        approach -> 
        iterate through array. for each element we find 0 - element as target. run a two pointer for that
        time complexity is O(n^2) with O(1) space
        we sort each array and check if it already exists in the answer array. if no, append.
        unsorted list so we run sort first O(nlogn)
        """
        nums.sort()
        answers = []
        for index, num in enumerate(nums):
            #if more than 0 in a sorted list, since we are only looking right, we know for sure it cannot add to 0
            if num > 0: return answers
            if index > 0 and num == nums[index-1]:
                continue

            target = 0 - num
            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    answers.append([num, nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1

                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1
        
        return answers