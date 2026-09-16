class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        return int(format(n, "032b")[::-1], 2)