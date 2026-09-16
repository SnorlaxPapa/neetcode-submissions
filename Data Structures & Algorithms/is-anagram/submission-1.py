class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seenS = dict.fromkeys(set(list(s)), 0)
        seenT = dict.fromkeys(set(list(t)), 0)

        for i in range(0, len(s)):
            seenS[s[i]] += 1
            seenT[t[i]] += 1
        
        for key, value in seenS.items():
            if seenT.get(key) == None or seenT[key] != value:
                return False

        return True
        