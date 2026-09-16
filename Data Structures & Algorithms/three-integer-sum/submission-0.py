class Solution:
    def twoSum(self, nums: List[int], currentPos: int, target: int) -> List[List[int]]:
        """
        two sum avoiding current position. possibility that there may be more than one solution. so we make a list
        """
        left = 0
        right = len(nums) - 1
        answers = []
        while left < right:
            #first make sure we are not using the current element
            if left == currentPos:
                left += 1
                continue
            if right == currentPos:
                right -= 1
                continue
            
            #standard twoSum
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
            target = 0 - num
            candidates = self.twoSum(nums, index, target)
            for candidate in candidates:
                if candidate not in answers:
                    answers.append(candidate)
        
        return answers