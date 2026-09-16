class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        given an array of unique numbers, we must return every possible combination
        the order of the elements does not matter, so [2, 3] is the same as [3, 2] 
    
        so we can run a prefix matching algorithm to search for subsets with the following rules
        1) we recursively search in front of the current element (as any combination with elements behind would've been searched)
        2) if our current combination is not in the answer, we add to it
        3) our return condition is simply when it hits the end of the array
        """

        result = [[]]
        
        def search(curr_index, prefix): 
            #return if we're at the end of the list
            if curr_index == len(nums):
                return

            nonlocal result
            #we add our curr element to prefix, then pop it once we've searched through the remaining space
            prefix.append(nums[curr_index])
            result.append(prefix[:])

            for i in range(curr_index + 1, len(nums)):
                search(i, prefix)

            prefix.pop()

        for index, num in enumerate(nums):
            search(index, [])

        return result