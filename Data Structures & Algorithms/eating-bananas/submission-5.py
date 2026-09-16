class Solution:
    def determineHours(self, piles: List[int], k: int) -> int:
        """
        goes through each item in the pile. if divisible, time taken is straightforward. if k not factor, we find truncated result and add 1
        """
        hours = 0
        for pile in piles:
            if pile % k == 0:
                hours += pile/k
            else:
                hours += pile//k + 1
        
        return hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        my understanding is that I am given a time limit, h, that I have to eat
        all the bananas in the array. 
        if the pile has more than my rate k, i would need p//k + 1
        if the pile is less than rate k, i'm unable to move on to another pile
        the lower the k, the longer time is taken
        logically, k need not exceed the maximum value of the array as eating more than the pile does not provide speed bosts
        we assume that h is always possible, for e.g. it will not be [1, 1, 1, 1] h = 3 as the qn did not specify what to return in the event it isnt

        my first instinct is to sort and find the maximum of the array and set it as k, and continuously iterate downwards by 1,
        calculating the time needed to finish all the piles.

        i then find the threshold at which i am unable to finish all piles and the k before that is the response

        in this instance, the worst case is O(n^2), in which the k is actually the minimum of the array (say, for an unbelievably large h)
        and we iterate from max -> min where each element is unique

        but if instead of incrementally finding k, what if we were to find it via binary search?

        we create an array of range [minArray, maxArray]
        our goal is then to find the minimum possible value for which time is within limit h
        we proceed with a binary search to find an acceptable number first 
        after that, we continue finding acceptable numbers to the left and save the lowest seen
        return lowest seen at the end
        
        runtime -> fixed splitting of array into 2 until the end, logn, each pass through n iterations. nlogn worst case
        sort is also nlogn

        why do we need minArray, maxArray?
        some solutions may have solutions that dont exist within simply piles
        for example, 
        piles = [3, 6, 7, 11] k = 4 (i didnt think of myself i saw it in the test case)


        but then how do we do it in O(1). simple, we dont even need an array. the array is in range 1, to max. we can just use simple calculations
        we can just use a O(n) pass to find max instead actually
        """
        
        left = 1
        right = max(piles)

        k = 99999999999999999
        while left <= right:
            middle = (right+left)//2
            hours = self.determineHours(piles, middle)
            if hours <= h: 
                k = middle
                right = middle - 1
            else:
                left = middle + 1

        return k