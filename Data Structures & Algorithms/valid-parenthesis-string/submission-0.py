class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0

        for paranthesis in s:
            if paranthesis == "(":
                minLeft += 1
                maxLeft += 1
            elif paranthesis == "*":
                minLeft -= 1
                maxLeft += 1
            else:
                minLeft -= 1
                maxLeft -= 1
            if minLeft < 0: minLeft = 0

            if maxLeft < 0: 
                return False

        return minLeft == 0