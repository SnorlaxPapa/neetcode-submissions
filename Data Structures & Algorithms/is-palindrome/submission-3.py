class Solution:
    def isValid(self, s: str) -> bool:
        if s == " " or (not s.isnumeric() and not s.isalpha()):
            return False
        return True


    def isPalindrome(self, s: str) -> bool:
        """
        remember to take note of different cases:
        both sides non-alphanumeric
        one side non-alphanumeric
        different capitalization but same char
        different breakpoints for odd and even
        """
        left = 0
        right = len(s) - 1
        if len(s)%2 == 0: middle = len(s)/2 
        else: middle = (len(s)-1)/2

        while left != middle:
            print(left)
            if self.isValid(s[left]) == False and self.isValid(s[right]) == False:
                left+=1
                right-=1
                continue
            if self.isValid(s[left]) == False:
                left+=1
                continue
            if self.isValid(s[right]) == False:
                right-=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        
        return True