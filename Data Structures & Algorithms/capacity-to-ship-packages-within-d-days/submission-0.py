class Solution:
    def testShip(self, weights: List[int], capacity: int, days: int) -> int:
        num_ships = 1
        curr_capacity = 0
        for weight in weights:
            curr_capacity += weight
            if (curr_capacity > capacity):
                num_ships += 1
                curr_capacity = weight
        
        return num_ships



    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #ship minimally needs the maximum weight of all the packages
        #maximum is total weight of the thing

        left = max(weights)
        right = sum(weights)
        res = right

        while (left <= right):
            middle = left + (right - left) // 2

            num_ships = self.testShip(weights, middle, days)
            if (num_ships <= days):
                res = min(middle, right)
                right = middle - 1
            else:
                left = middle + 1

        return res

