class KthLargest:
    """
    maintain a k sized min-heap. this basically maintains the top k elements up to k
    when our heap has more than k elements, we pop the min 
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = []
        
        for num in nums:
            self.add(num)

        while len(self.heap) > k:
            self.extract()


    
    def extract(self):
        #replace root with last element. then keep swapping down with the smaller child until no longer smaller than smaller child
        if len(self.heap) == 1:
            self.heap = []
            return

        last = self.heap.pop()
        n = len(self.heap)

        self.heap[0] = last

        i = 0

        while True:
            smallest = i
            left = i * 2 + 1
            right = left + 1

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest


    def add(self, val: int) -> int:
        #if k is at capacity, we only add is this new val is greater than our top kth
        if len(self.heap) == self.k:
            if val < self.heap[0]: return self.heap[0]
            self.extract()

        #to add, we insert the element at the bottom, then keep swapping up to its parent then we return the min root
        i = len(self.heap)
        self.heap.append(val)
        while i > 0:
            parent = (i - 1)//2
            if self.heap[i] < self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[i]
                self.heap[i] = temp
                i = parent
            else:
                break

        return self.heap[0]

        
