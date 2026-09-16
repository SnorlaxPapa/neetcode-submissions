class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        maintain a monotonic decreasing stack.
        if the newest element is greater than top element, we pop and add latest to the stack
        if not, we add to the stack no popping
        everytime we pop, we take the difference in index when popping as results[day]
        """
       
        if len(temperatures) == 1: return [0]

        results = [0 for _ in range(len(temperatures))]
        stack = [] #pair temp, index

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackInd = stack.pop()
                results[stackInd] = index - stackInd

            stack.append((temperature, index))

        return results


