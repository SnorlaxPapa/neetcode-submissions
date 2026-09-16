class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        this question reminds me of the most rainwater trapped question. where we have two pointers and we just iterate the smaller value inwards
        but this time, we are limited by rectangles inside being smaller which will affect us. two pointers can be used here

        let us do a left to right pass
        we iterate down.
        when we see a shorter bar, we need to recompute the current area starting from the current leftbound. 
        we shouldn't start a new rectangle when we see a shorter bar because our width will be greater, just cap at the new max
        this can be done if we save the index of the left bound somewhere

        but what if we encounter a larger bar?
        we have two options: 
        we can
        1) create a new rectangle while maintaining tracking of the old one
            - so we can have an array of leftBound in the form [(leftBoundIndex, shortestBar, maxArea)]
            then everytime we encounter a shorter bar then our shortestBar, we can set that as rightBound and calculate area. If area > maxArea, we can replace
            - then everytime we meet a shorter bar, we just iterate through leftBound and calculathe areas
            - everytime we meet a largerBar, we create a new leftBound entry of (index, height, height)

            What is the worst case for this? A strictly increasing array of bars
            [1, 2, 3, 4, 5, 6, 7, 8]
            so in this case, 
            each time we encounter a new taller bar, we are increasing length of leftBound by 1
            that means we are doing 1+2+3+...+7 -> (n-1)*n/2 iterations which is O(n^2)
            
            how can we keep to O(n)

        2) we keep a monolithic increasing stack. if bar is >= latest stack, that means rectangle can keep going
        - if bar is shorter, then that means its the end of this specific rectangle
            we keep popping arrays in the stack until we find a bigger one, computing the area for each popped one. we then push the element with its index being the last bar it popped (because it can expand all the way there)
            why does this work: if the bar is shorter, that means that any taller bars cannot 'grow'anymore. any future calculations will have to be done with this new smaller bar, so we pop everything.
            if the bar is taller, that means that 'smaller'left bound can keep progressing. 
        - if the bar is taller, we add it to the stack
        
        time complexity - each element can be pushed onto the stack exactly once, and at most can be popped once. so by that logic at most we have 2n operations. time complexity O(n)
        """

        maxArea = 0
        stack = []

        for index, bar in enumerate(heights):
            if index==0: 
                stack.append((index, bar))
                maxArea = bar
                continue

            if bar >= stack[-1][1]:
                stack.append((index, bar))
            else:
                lastIndex = 0
                while stack and bar < stack[-1][1]:
                    lastIndex = stack[-1][0]
                    area = (index - lastIndex) * stack[-1][1]
                    maxArea = max(area, maxArea)
                    stack.pop()
                stack.append((lastIndex, bar))

        #for leftover in the stack
        for bar in stack:
            area = bar[1] * (len(heights) - bar[0])
            maxArea = max(area, maxArea) 

        return maxArea
                    