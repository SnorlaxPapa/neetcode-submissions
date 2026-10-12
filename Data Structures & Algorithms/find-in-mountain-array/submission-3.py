class Solution:
    def binarySearch(self, is_left: bool, target: int, middle: int, mountainArr: 'MountainArray') -> int:
        left = 0 if is_left else middle + 1
        right = middle - 1 if is_left else mountainArr.length() - 1

        while (left <= right):
            middle = left + (right - left) // 2

            val = mountainArr.get(middle)
            if val == target:
                return middle
            
            if val > target:
                if is_left:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if is_left:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """basically asking if within a mountain shaped array, a specific number exists. so we can do this by starting in the middle
        
        we start with a binary search for the target

        following cases
        middle == target -> good ! ideally first match is the first occuring index by our search 
        middle > target 
        middle < target
        so we know there is a portion of the array that is strictly increasing, and that there is a portion that is strictly decreasing
        
        we need to decide which half we can confidently continue searching in
        to do that we need to know which half of the mountain we're on

        so we find where the peak is first with binary search.
        then we do a binary search on the left half and right half
        """

        #we first do a binary search to find a peak
        left = 0
        right = mountainArr.length() - 1
        peak = -1
        index_peak = -1

        while (left <= right):
            middle = left + (right - left) // 2
            candidate = mountainArr.get(middle)
            nxt = mountainArr.get(middle + 1)

            if candidate > nxt:
                #we need to go back to ascend the mountain
                right = middle - 1

            else:
                #we need to go forward to ascend the mountain
                left = middle + 1
        
        if mountainArr.get(left) == target: return left

        left_pos = self.binarySearch(True, target, left, mountainArr)
        if left_pos != -1: return left_pos

        right_pos = self.binarySearch(False, target, left, mountainArr)

        return right_pos



        