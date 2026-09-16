class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        initial intuition: 
        have the results array track hottest day, and aas we iterate down the array we append to each tracker in results and stop adding when we find a hotter day
        but this would be O(n^2) worst case in time and space because might have N*(N+1)/2 elements and iterations in a strictly descending temperature
        
        return [0] if len 1
        what if i send it backwards?

        if its greater than the previous one, then we set result[i-1] = 1
        if its not, then we set a max stack
        so e.g.
        36, 35, 40, 28

        start at 28. 28 is appended to max stack
        28 is not greater, result[4] = 0, result[3] = 0. 28 is popped from max stack and 40 is added. 
        then we hit 35, compare 35 with [-1] of maxstack. 35 is smaller so we append it maxstack and set result[2] = 1
        then we hit 36, incrementally compare with maxStack. first hit 35. 35 is smaller. 
        we increment and pop until we find a bigger element. track the number of pops
        in this case we hit 40, then append 36. anyways u get the gist

        iterate backwards, maintain greaterTemp stack, pop if encounter greater element
    
        O(n) in space (because we are at most holding n temps in the stack) and O(n) in runtime
        strictly ascending -> O(n) space but iteration will stop at the first element

        i realized this will not work if its a sequence like 38, 30, 36, 35, 40 35 will be popped. so scan will be like 30 36 40
        """
        if len(temperatures) == 1: return [0]
        
        greaterTemp = [temperatures[-1]] 
        results = [0 for _ in range(len(temperatures))]

        position = -2
        for temperature in reversed(temperatures[:-1]):
            print(temperature, ": ", greaterTemp)
            exist = False
            counter = 1
            for greater in reversed(greaterTemp):
                if temperature >= greater:
                    counter+=1
                    print("yo ", counter)
                elif temperature < greater:
                    print("hello!")
                    greaterTemp.append(temperature)
                    results[position] = counter
                    print("final: ", counter)
                    exist = True
                    break

            if exist==False: #means no greater temperature exists:
                print("hi!")
                results[position] = 0
                greaterTemp.append(temperature)
            
            position-=1

        return results

