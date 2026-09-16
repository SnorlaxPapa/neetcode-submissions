class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        naive sol: iterate through every element
        and then for each element, i iterate through the elements in front of it and track the max profits 
        O(n^2) solution

        is there any way to complete it one pass? 
        actually we can use a max stack but troublesome to implement, and it is not O(1) space

        what if we looked backwards?
        suppose we iterate through the array. with each i, we must decide which day we want to sell it on?
        so suppose [10,1,5,6,7,1]
        we start i = 1. we look left, do we want to sell no? we move forward to i = 2 and look left, we see 1. yes sell! we keep track of this
        selling value. then we keep shifting our i and comparing to our left. if our prices[i] - prices[i-1] > prices[i] - lowestPrice, then we replace lowestPrice with prices[i - 1]
        then we return the max profit with default being 0
        """

        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i-1] < lowest_price: lowest_price = prices[i-1]
            max_profit = max(prices[i] - lowest_price, max_profit)

        return max_profit
