class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        110213

        first character 
        1 1 way 2 way
        second character
        1 2 
        12 
        2 ways 
        third character
        number of ways to reach character before it if it is not a 0
        number of ways to reach characters before it if previous num is not a 0

        to generalize

        n = (n - 1) if [n] != 0 else 0 + (n - 2) if [n-1] != 0 and the combination is less than 26

        at 0 
        valid, can only take n-2 so 1

        at 2
        0 2 is invalid so only valid combination is from n-1 which is 1

        at 1

        can either be formed from n-1 or n-2 as 21 and 1 are valid, so 1 + 1 = 2

        at 3,
        can either be formed from prev 1 (2) or from prev 2 (1) == 3
        """
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        
        prev_prev = 1
        if s[1] == "0":
            if int(s[0:2]) > 26: return 0
            prev = 1
        else: 
            if int(s[0:2]) > 26: 
                prev = 1
            else: 
                prev = 2

        for i in range(2, len(s)):
            if s[i] == "0":
                if int(s[i-1]) > 2 or s[i-1] == "0": return 0 #invalid combination
                curr = prev_prev
            else:
                if s[i-1] == "0" or int(s[i-1:i+1]) > 26:
                    curr = prev
                else: 
                    curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return prev
                
                