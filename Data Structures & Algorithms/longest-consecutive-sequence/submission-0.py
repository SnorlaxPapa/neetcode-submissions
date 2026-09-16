class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        if duplicate numbers, we take only one
        if empty array, we return 0

        Given O(n) time, we need to be able to complete the process in kn iterations
        naive solution is to sort the array, but this is generally O(nlogn)

        Instead, we can use a seen substring hashmap. then we can join the subsequences

        e.g.
        [0, 3, 2, 5, 4,  6, 1, 1] -> [[0, 1], [3, 4], [2], [5, 6], [4]]
        fk me a set is O(1) lookup
        """
        
        if len(nums) == 0: return 0

        setNums = set(nums)
        seenNums = set()
        longest = 0

        for num in nums:
            longestStreak = 1
            if (num - 1) not in seenNums:
                nextNum = num + 1
                seenNums.add(num)

                while nextNum in setNums:
                    longestStreak += 1
                    nextNum += 1
                    seenNums.add(nextNum)

                if longestStreak > longest:
                    longest = longestStreak
        
        return longest


        