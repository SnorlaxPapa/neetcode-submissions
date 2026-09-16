class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area is calculated by distance between two bars * min(b1, b2)
        we can use a two pointer approach. we start on the L R edges
        what is the condition to change L and R?
        we increment the smaller height toward the center. reason being if we increment the larger height, 
        we will forever be capped at the smaller height, and  max area will never increase

        so for example
        [1, 7, 2, 5, 4, 7, 3, 6]
        1, 6 -> 7, 6 -> 7, 3 ...
        track max height

        for [2, 2, 2]
        if we use a strict inequality (gt), then we will never increment.
        we can standardize to incrementing the left side 

        why can we standardize to incrementing a specific side? 
        since both heights are similar, we know that any subsequent max_height 
        will be <= curr_height, and hence area will always be smaller
        in fact, by above logic we can increment both L and R when they are same
        """ 

        left = 0
        right = len(heights) - 1
        maxHeight = -1
        
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxHeight = max(maxHeight, area)
            #handle when both heights are the same
            if heights[left] == heights[right]:
                left+=1
                right-=1
            elif heights[left] > heights[right]:
                right-=1
            else:
                left+=1
            
        return maxHeight
            




