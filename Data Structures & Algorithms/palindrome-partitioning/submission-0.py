class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def search(prefix, index):
            if len("".join(prefix)) == len(s):
                result.append(prefix[:])

            for i in range(index+1, len(s)+1):
                if s[index:i] == s[index:i][::-1]:
                    prefix.append(s[index:i])
                    search(prefix, i)
                    prefix.pop()

        search([], 0)

        return result