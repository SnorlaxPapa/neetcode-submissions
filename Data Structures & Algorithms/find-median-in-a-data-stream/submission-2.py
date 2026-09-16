import heapq

class MedianFinder:
    """
    intuitive solution:
    add number -> insert to a sorted array in O(logn) with a binary search, time O(nlogn) for n elements
    find median -> extracts median in O(1) time

    Bottleneck: Add number takes too long. Data structure needs to append faster
    What if we use quick select? O(1) for addNum, O(N) for findMedian (we simply set the pivot at the median position and partition the elements around it)
    
    It would be smoother if findMedian was O(1) while addNum took longer
    What if we maintain a min-heap?
    children are always >= parent

    Within an array, to find the median
    all we need to care about is the maximum of the left half and the minimum of the right half
    so we maintain two heaps, one left maxheap, one right min heap
    for even medians, we can take the left and the right
    for odd medians, we take the max of the heap with the larger size
    left max can never be greater than right min

    at each step, 
    we check if num > right min (if it exists). if it is, we push it to the right stack
    if not, we push it to the left stack

    if the size of the heaps differ > 1, we pop and push to the smaller heap
    """
    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if self.right_min and num > self.right_min[0]:
            heapq.heappush(self.right_min, num)
        else:
            heapq.heappush(self.left_max, -1 * num)

        if len(self.left_max) - len(self.right_min) > 1:
            left_val = -1 * heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, left_val)
        elif len(self.right_min) - len(self.left_max) > 1:
            right_val = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -1 * right_val)
        
        
    def findMedian(self) -> float:
        if (len(self.left_max) + len(self.right_min)) % 2 == 0:
            return (-1 * self.left_max[0] + self.right_min[0])/2
        else:
            median = -1 * self.left_max[0] if len(self.left_max) > len(self.right_min) else self.right_min[0]
            return median
        
        