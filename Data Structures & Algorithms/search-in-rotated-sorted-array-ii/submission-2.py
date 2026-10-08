class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        one side of the array must be sorted, so we just find the side where either left < middle or middle > right. then search in that area before searching in the other side. 
        now there are duplicates within the array
        so for
        3 4 4 5 6 1 2 2

        we start with 3, 2
        we operate still und the assumption that one half is still not broken. 
        
        """

        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = left + (right - left) // 2
            if (nums[mid] == target): return True

            if nums[left] < nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[left] > nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                left += 1


        return False