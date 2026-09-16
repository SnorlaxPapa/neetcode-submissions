class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1 if x > 0 else 2**31
        is_neg = x < 0
        x = abs(x)
        tens = len(str(x)) - 1  

        res = 0
        while x:
            last_digit = x % 10
            x = x // 10

            res = res * 10 + last_digit
            if res > MAX: return 0
        res = -1 * res if is_neg else res
        
        return res

            
