class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #handle edge case of empty digits
        if len(digits) == 0: return []
        
        #initialize our results array
        results = []

        #initialize our hashmap
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        #write a recursive dfs search function that processes each digit step by step
        def search(prefix, index):
            #return if whole string processed
            if index == len(digits):
                results.append("".join(prefix))
                return

            #recursively search through our combinations
            number = digits[index]
            for char in phone[number]:
                prefix.append(char)
                search(prefix, index+1)
                prefix.pop()

        
        search([], 0)
        
        return results


