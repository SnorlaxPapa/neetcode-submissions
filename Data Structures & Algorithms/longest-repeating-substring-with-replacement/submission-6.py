class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        we should keep track of max_freq, and a hashmap to count frequencies of all char in a sliding window
        we have two LR pointers starting at 0
        each time R pointer moves, we first update its count
        then we check if this new freq > the max freq we have stored
        aft wards, we check validity of array by finding length - max_freq and checking if > k
        if it is, we move L pointer forward
        then we update maxLength
        """

        left = 0
        max_length = 1
        char_count = {}
        max_freq = 0

        for right in range(0, len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1 
            max_freq = max(max_freq, char_count[s[right]])

            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(right - left + 1, max_length)

        return max_length