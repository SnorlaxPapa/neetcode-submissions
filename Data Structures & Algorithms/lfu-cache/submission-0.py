class LFUCache:

    def __init__(self, capacity: int):
        self.key_freq_map = {}
        self.freq_keys_map = {}
        self.min_freq = 1
        self.capacity = capacity
        self.kv = {}


    def get(self, key: int) -> int:
        if key not in self.kv: return -1
        self.increment_freq(key)

        return self.kv[key]
        

    def delete(self):
        key = next(iter(self.freq_keys_map[self.min_freq]))
        self.freq_keys_map[self.min_freq].pop(key)
        self.kv.pop(key)
        self.key_freq_map.pop(key)

        if (len(self.freq_keys_map[self.min_freq]) == 0):
            self.freq_keys_map[self.min_freq]
            #deletion only happens when new key is being inserted, so we can safely set min freq to 1
            self.min_freq = 1


    def increment_freq(self, key) -> None:
        #update key frequency with key frequency map
        freq = self.key_freq_map.get(key, 0)
        self.key_freq_map[key] = freq + 1
        new_freq = self.key_freq_map[key]
        self.min_freq = min(new_freq, self.min_freq)

        #update frequency key map
        if new_freq in self.freq_keys_map:
            self.freq_keys_map[new_freq][key] = 0
        else:
            self.freq_keys_map[new_freq] = {key: 0}
        
        #update old frequency mapping
        if freq != 0: 
            self.freq_keys_map[freq].pop(key)
            if (len(self.freq_keys_map[freq]) == 0):
                self.freq_keys_map.pop(freq)
                if freq == self.min_freq:
                    self.min_freq = new_freq;


    def put(self, key: int, value: int) -> None:
        #if our capacity is full (i.e. len of kv = capacity, we need to call the delete ops, we can exploit the insertion order in dictionary to simply remove the first element)
        if key not in self.kv and len(self.kv) == self.capacity:
            self.delete()
        
        self.kv[key] = value
        self.increment_freq(key)



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)