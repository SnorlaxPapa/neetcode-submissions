class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        given array of unqiue integers, we need to return all possible permutations

        we can do this by using the whole array as a search space except its own position
        so 1 will scan 2 3, 2 will scan 1 3, 3 will scan 1 2.

        we recursively scan, with a parents set that indicates whether or not it's already been used, then append it to our results once len(prefix) == len(array)

        at each node, we have (n-k) choices, where k is the depth of our search tree. our depth is n so space is O(n), and time complexity will be O(n * n!) 

         it uses $O(n)$ extra auxiliary space for the parents set and the prefix list. Can you generate all permutations in-place by mutating the original nums array to achieve $O(1)$ extra space (excluding the call stack)?"
        """
        results = []
        def search(prefix, parents):
            #if we have found a permutation, append and return
            if len(prefix) == len(nums):
                results.append(prefix[:])
                return

            #if we are still short, 
            for i in range(0, len(nums)):
                if nums[i] not in parents:
                    parents.add(nums[i])
                    prefix.append(nums[i])

                    search(prefix, parents)

                    parents.discard(nums[i])
                    prefix.pop()

        search([], set())

        return results
