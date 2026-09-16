class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if count.get(num) == None:
                count[num] = 1
            else:
                count[num] += 1
        
        sortedList = sorted(count.items(), reverse=True, key=lambda x: x[1])

        answer = []
        for i in range(0, k):
            answer.append(sortedList[i][0])
        
        return answer