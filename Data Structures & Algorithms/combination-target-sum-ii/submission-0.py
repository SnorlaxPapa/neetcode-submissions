class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def search(index, prefix, curr_sum):
            if curr_sum == target: 
                results.append(prefix[:])
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if curr_sum + candidates[i] > target:
                    break
                
                prefix.append(candidates[i])
                search(i + 1, prefix, curr_sum + candidates[i])
                prefix.pop()

        candidates = sorted(candidates)
        search(0, [], 0)

        return results
            