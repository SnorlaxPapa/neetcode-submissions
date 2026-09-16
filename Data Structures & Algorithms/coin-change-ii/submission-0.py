class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #populate our possible combinations
        combinations = [0 for _ in range(amount + 1)]
        combinations[0] = 1
        
        for coin in coins:
            i = 0
            for curr in range(coin, amount + 1):
                combinations[curr] += combinations[curr - coin]

        return combinations[amount] 
                

