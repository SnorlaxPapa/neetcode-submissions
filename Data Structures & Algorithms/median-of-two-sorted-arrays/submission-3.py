class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        naive solution, use a two pointer starting at nums1 and nums2 0 index, count steps down until hit the median

        median value -> the middle value
        two cases, odd or even 
        must run in log(m+n) time

        [1, 3] [2, 4]
        log(m+n) runtime -> split arrays into two and run a dc/binary search approach
        but how do we split the array into two?

        iterate thru nums 1, binary search next biggest number in nums 2, then insert into nums 1, then find median
        this will be mlogn 

        how do we this in one pass through? 
        when we combine the arrays, we have two striclty sorted ascending arrays in [ 1 3 5 7 |  2 4 6 8 10]

        what do we know? 
        we know that the median is at the (m+n)//2th element for odd total, and the mean of the (m+n)/2th + (m+n)/2 - 1 th elements

        that means that from the two arrays, we should select specifically (m+n)//2 elements 
        for above 8 element array it would mean first 4 elements in the combined array
        so it could be 2 from nums1, 2 from nums2, or 1 3 or 0 4
        how do we find the correct split of arrays?

        so we start with an initial even split of parititons (e.g. 2 2)
        we know aleft < aright and bleft < bright
        we need to check that 
        aleft<=bright and bleft<=aright so we know that the left side is truly smaller than the right side
        in this case,
        left = 0
        right = len(nums1) - 1
    
        we are operating on the premise that nums1 length > nums2, if its not, we callt his function with arrays swapped

        while left <= right:
            partitionA = left + right // 2
            then we find a left b left a right b right
            if both a left and b left aare smaller than b right and a right respectively, we know this is the correct partititon
            if not, there are two possibilities
            aleft > bright
            means our nums1 selection is too large. we do right = partitionA - -1
            bleft > aright
            means our nums1 selection is too small, we do left = partitionA + 1
        """ 
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        totalLength = len(nums1) + len(nums2)
        halfTotal = (totalLength + 1)//2

        left = 0
        right = len(nums1) 

        while left <= right:
            partitionA = (left+right)//2
            partitionB = halfTotal - partitionA 

            aLeft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            aRight = nums1[partitionA] if partitionA < len(nums1) else float("inf")

            bLeft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
            bRight = nums2[partitionB] if partitionB< len(nums2) else float("inf")

            if aLeft <= bRight and bLeft <= aRight: 
                if totalLength % 2 == 0:
                    return (min(aRight, bRight) + max(aLeft, bLeft)) / 2
                else:
                    return max(aLeft, bLeft)
            if aLeft > bRight:
                #means our nums1 partition is too big
                right = partitionA - 1
            elif bLeft > aRight:
                #means our nums1 partition is too small
                left = partitionA + 1
