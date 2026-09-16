class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        maintain a seen dict with key: char and value: index
        we start with sliding window L = 0 R = 1
        each time we move forward, 
        we check if the new char is in the seen dict. if no, we save its position and save the longest substring
        if yes, we iteration L to the position in front of the saved index, each time removing the left bound keys from the seen dict (to remove them)
        this will be O(n) runtime and O(m) space
        """
        if s=="": return 0

        seenDict = {s[0]: 0}
        left = 0
        maxLength = 1
        for right in range(1, len(s)):
            if s[right] in seenDict and seenDict[s[right]] >= left:
                left = seenDict[s[right]] + 1
            else:
                maxLength = max(maxLength, right - left + 1)
            seenDict[s[right]] = right
        
        return maxLength

                