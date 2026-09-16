import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        maintain a heap. at each step, we take the two latest stones (heappop)
        compare them, then heappush the remaining stone (if any) to the heap
        until we have 1 stone left
        we must maintain a max heap. to do so with built-in library, we need to make the numbers negative
        """
        #negative numbers
        for i in range (len(stones)):
            stones[i] = -1 * stones[i]

        #heapify
        heapq.heapify(stones)

        #smash stones until one remains
        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)

            if stone_one == stone_two:
                continue
            
            new_stone = -1 * abs(stone_two - stone_one)
            heapq.heappush(stones, new_stone)
        
        if stones: return abs(stones[0])
        return 0