class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        when merging triplets,
        we know we cannot safely merge i and j if any of the elements in j is greater than our target
        if all elements in the merged i and j are <= target, then we can merge
        """

        prev = [float("-inf"), float("-inf"), float("-inf")]

        for triplet in triplets:
            valid = triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]
            if not valid: continue

            prev[0] = max(prev[0], triplet[0])
            prev[1] = max(prev[1], triplet[1])
            prev[2] = max(prev[2], triplet[2])

            if prev[0] == target[0] and prev[1] == target[1] and prev[2] == target[2]: return True

        return False