import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(bit) for bit in bin(n)[2:])