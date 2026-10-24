class Solution:
    def tribonacci(self, n: int) -> int:
        previous = [0, 1, 1]

        if (n <= 2): return previous[n]

        i = 3
        while (i <= n):
            new = previous[0] + previous[1] + previous[2]
            previous[0] = previous[1]
            previous[1] = previous[2]
            previous[2] = new
        
            i += 1
        
        return new