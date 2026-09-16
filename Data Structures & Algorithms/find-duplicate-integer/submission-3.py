class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #we find the common position this loop will end up at the first position they meet
        #where nums[slow] == nums[nums[fast]]
        while nums[slow] != nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = nums[nums[fast]]
        #once we find common position, reset 0 and increment both forward to find duplicate num
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        
        return nums[slow]
        