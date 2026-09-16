class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        given an array of unique numbers, we must return every possible combination
        the order of the elements does not matter, so [2, 3] is the same as [3, 2] 
    
        so we can run a prefix matching algorithm to search for subsets with the following rules
        1) we recursively search in front of the current element (as any combination with elements behind would've been searched)
        2) if our current combination is not in the answer, we add to it
        3) our return condition is simply when it hits the end of the array

        for our complexity analysis,
        each of our search is guaranteed to be a hit, so that means there are 2 ** n searches. For each search, we spend worst case n time copying the string
        So our time complexity is (n*2^n)

        Each search warrants one recursive call, which means our space complexity is (n*2^n)
        """

        result = []
        
        def search(curr_index, prefix): 
            #append our current prefix
            nonlocal result
            result.append(prefix[:])

            for i in range(curr_index, len(nums)):
                prefix.append(nums[i])
                search(i+1, prefix)
                prefix.pop()

        search(0, [])

        return result