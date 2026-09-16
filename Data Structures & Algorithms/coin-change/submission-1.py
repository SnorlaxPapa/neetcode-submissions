from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        visited = set()

        coin_q = deque([(amount, 0)])
        while(coin_q):
            curr, coin_amount = coin_q.popleft()
            if curr in visited: continue
            visited.add(curr)

            for coin in coins:
                if curr == coin:
                    return coin_amount + 1
                if curr > coin:
                    coin_q.append((curr - coin, coin_amount + 1))

        return -1


