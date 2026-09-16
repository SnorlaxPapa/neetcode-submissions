import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []

        #process elements one by one in a k-size min-heap. 
        for num in nums:
            heapq.heappush(result, num)

            #pop if size > k 
            if len(result) > k:
                heapq.heappop(result)
        
        return result[0]