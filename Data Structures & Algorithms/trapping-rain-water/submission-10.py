class Solution:
    def trap(self, height: List[int]) -> int:
        """
        two pointer solution
        left and right bound
        track leftMax and rightMax
        incrememnt smaller pointer value inwards
        each step, add that sides tallest wall - curr height to area as we know for a fact the other wall is taller, so definitelty this water can be added.
        doesn't matter if subsequent step in that direction is taller than current max, still limited by curr smaller max
        """
        if len(height) <= 2: return 0

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        area = 0

        while left < right:
            if height[left] >= height[right]:
                right-=1
                area += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
            else:
                left+=1
                area += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])

        return area

        