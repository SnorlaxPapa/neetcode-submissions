class Solution:
    def calculateTime(self, target: int, position: int, speed: int) -> float:
        distanceLeft = target - position
        return distanceLeft/speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        we have n different cars of index i {0<=i<n} with a position and a speed array where 
        position[i] and speed[i] correspond to the ith car's position n speed respectively

        car fleet: as long as the car behind has a greater speed, it will catch up to the car in front
        the question is is the car able to catch up to the car in front by the time we before or exactly when we hit the target?

        if it can, then we can constitute it as part of the car fleet. if not, it is likely another car fleet

        what if it cannot catch up to the car in front, but instead another much slower travelling car fleet ahead that's ahead of the cars in front of it?
        doesn't matter, as it cannot overtake. so we only need to be concerned about the car in front

        so my initial instinct is to traverse backwards

        first how to calculate whether or not it can catch up to the carfleet given the current position and speed?
        we can simply calculate if the distance left/speed for curr car is <= the same calculation for the car fleet

        we can maintain a stack of car fleets, with the latest element being the next car fleet's calculated value. if our current car value is smaller than that, we can append it to the stack as a new caar fleet
        just return len of the car fleet

        we can do this because the car fleet is limited by the front car

        we should combine position and speed into (position, speed) and sort by position for this to work
        """
        if len(position) == 1:
            return 1

        orderedCars = []
        for i in range(len(position)):
            orderedCars.append((position[i], speed[i])) #store as (position, speed)
        orderedCars.sort(key=lambda x: x[0])
        print(orderedCars)

        carFleet = [self.calculateTime(target, orderedCars[-1][0], orderedCars[-1][1])]
        print(carFleet)
        for car in range(len(orderedCars) - 2, -1, -1):
            timeNeeded = self.calculateTime(target, orderedCars[car][0], orderedCars[car][1])
            print(timeNeeded)
            if timeNeeded > carFleet[-1]:
                carFleet.append(timeNeeded)
        
        return len(carFleet)