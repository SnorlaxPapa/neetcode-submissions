import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we run a binary search style partition
        left = 0
        right = len(nums) - 1

        while left <= right:
            #calc partition
            pivot = (left + right)//2

            #shift > values to left of pivot, <= to right, swap first to prevent unexpected behaviour
            nums[pivot], nums[right] = nums[right], nums[pivot]
            swap = left
            pivot = right

            for i in range(left, right):
                #if greater than pivot, we swap to left side. if <= leave swap as is
                if nums[i] > nums[pivot]:
                    nums[i], nums[swap] = nums[swap], nums[i]
                    swap += 1
                
            nums[swap], nums[right] = nums[right], nums[swap]
            pivot = swap
            
            #change boundaries based on left elements
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                left = pivot + 1
            elif pivot > k - 1:
                right = pivot - 1
            

 