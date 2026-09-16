class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        power_of_two = 1

        for i in range(1, n + 1):
            if power_of_two * 2 == i:
                power_of_two = i

            remainder = i - power_of_two
            dp[i] = 1 + dp[remainder]

        return dp

            