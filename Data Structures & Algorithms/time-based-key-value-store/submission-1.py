class TimeMap:
    """
    time-based key-value data structure
    key: key 
    value: value w time stamp
    set will store the key, get will get the key
    O(1) for set, O(logn) for get
    time stamp is given in the form int
    O(m*n) space n is the values associated with a key, and m is the total number of keys
    so the time stamp shouldn't take up additional space
    
    get works like this: given a get timestamp for the key, we must return the value with the largest timestamp that is <= input timestamp, 
    and if such a timestamp does not exist, then we return ""

    O(1) for set means we cannot sort the array during insertion, and retrieval must be done on the fly w the data structure we built within logn time

    so we can have a 
    {key: value} what is the value? 
    if we have a list of values in increasing order 
    oh nvm timestamps are set in increasing order
    
    structure will be {key: [(timestamp1, value), (timestamp2, value)]}
    then we can use binary search for timestamps
    """
    def __init__(self):
        self.kvMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvMap:
            self.kvMap[key] = [(timestamp, value)]
        else:
            self.kvMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        if self.kvMap.get(key) == None: return ""
        right = len(self.kvMap[key]) - 1
        maxTimestamp = ""

        while left <= right:
            middle = (left + right)//2

            if self.kvMap[key][middle][0] > timestamp:
                #middle is greater than timestamp, so we must look left
                right = middle - 1
            else: 
                #middle is less than timestep. condition fulfilled. we keep looking right for bigger timestamps
                maxTimestamp = self.kvMap[key][middle][1]
                left = middle + 1

        return maxTimestamp


        
        
