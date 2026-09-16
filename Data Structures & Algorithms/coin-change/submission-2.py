from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        visited = {amount}

        coin_q = deque([(amount, 0)])
        while(coin_q):
            curr, coin_amount = coin_q.popleft()

            for coin in coins:
                if curr == coin:
                    return coin_amount + 1
                if curr > coin:
                    if (curr - coin) in visited: continue
                    coin_q.append((curr - coin, coin_amount + 1))
                    visited.add(curr - coin)

        return -1


