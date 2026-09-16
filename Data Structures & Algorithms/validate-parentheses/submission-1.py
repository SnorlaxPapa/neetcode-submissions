class Solution:
    def isValid(self, s: str) -> bool:
        """
        since it has to be in the same order it is closed, we can just do the following checks
        1) check if len(s) is even. if odd we know for sure its an open string
        2) iterate down the list, for each open bracket, we add to an open bucket list. when we encounter a closed bracket, just check if its equivalent to last in open. if it is, then just simply pop the last open. if not return false
        3) return True if done
        """
        if len(s) % 2 != 0:
            return False

        bracketPairs = {"(": ")", "{": "}", "[": "]"}
        seenOpen = []

        for bracket in s:
            if bracketPairs.get(bracket) != None:
                seenOpen.append(bracket)
            else:
                #exit conditions
                if len(seenOpen) == 0:
                    return False
                if bracketPairs[seenOpen[-1]] != bracket:
                    return False
                seenOpen.pop()
                
        
        return len(seenOpen) == 0
