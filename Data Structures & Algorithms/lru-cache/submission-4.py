class LRUCache:
    """
    with a LRU cache
    constraints: get O(1), put O(1), given capacity.
    put removes the least recently used key.
    objective is to find a way to track the least recently used key 
    Least recently used queue can be maintained via a queue intuitively for quick O(1) insertion and oldest key
    we can either use Python's built in deque implementation from collections, or create a linked list

    get requires O(1) lookup. if we use a linked list, it'll be O(n), similar for deque
    for a O(1) lookup, we need a dictionary or a set
    a linked list with a dictionary?
    k: [value, next_key, prev_key] next_key is None for msot recently added key and prev_key is None for head
    we track the head and the tail of the dictionary
    everytime get is run, assuming key is inside, we set head = head[1] (the next_key) and tail[1] = the key lookup, update tail

    if constraint is hit, we can just pop head
    O(1) lookup in O(1) space
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.LRU: return -1
        if len(self.LRU) == 1: return self.LRU[key][0]

        #a -> b -> c -> tail, get b, we assign a next to c, c prev to a, tail next to b, b next to none and prev to tail, we also need to handle get tail
        prev = self.LRU[self.LRU[key][2]] if self.LRU[key][2] is not None else None
        nxt = self.LRU[self.LRU[key][1]] if self.LRU[key][1] is not None else None
        if nxt == None: return self.LRU[key][0]

        tail = self.LRU[self.tail]

        if prev == None:
            nxt[2] = None
            self.head = self.LRU[key][1]
        else:
            prev[1] = self.LRU[key][1]
            nxt[2] = self.LRU[key][2]
        
        tail[1] = key
        self.LRU[key][2] = self.tail
        self.LRU[key][1] = None
        self.tail = key
        return self.LRU[key][0]

    def put(self, key: int, value: int) -> None:
        if self.head == None:
            #handle empty list
            self.LRU[key] = [value, None, None]
            self.head = key
            self.tail = key
            self.capacity -= 1
            return
        
        #check if key is in LRU with .get. if it is, it handles the job of shifting it to the front, and we can just change value
        if self.get(key) != -1:
            self.LRU[key][0] = value
        else: #handle addition of a new key
            self.capacity -= 1
            self.LRU[self.tail][1] = key
            self.LRU[key] = [value, None, self.tail]
            self.tail = key
        
        #handle overcapacity by popping old head and setting next head
        if self.capacity == -1:
            old_head = self.head
            self.head = self.LRU[old_head][1]
            self.LRU[self.head][2] = None
            self.LRU.pop(old_head)

            self.capacity += 1

        return
        






        
        
