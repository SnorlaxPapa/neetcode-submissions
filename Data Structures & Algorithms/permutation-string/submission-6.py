class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        we are given two strings. check if permutation of s1 in s2
        O(n) time and O(1) constraint
        we are checking for permutation, and we need to do it in one pass through
        we know that the permutation is a fixed length, so we can use a fixed length sliding window
        to check if the permutation exists in s2, with l - r + 1 being the length of the string
        where l r are the left right boundaries of the fixed window

        edge case? s1 length > s2? what happens then? we return false cuz qn states s1 in s2 and not converse

        we simply create a hashmap with k:v pair char: count. this is still O(1) because max growth is 26
        we first create the target hashmap with s1 counts
        we then create a counting hashmap for our window
        for our initial fixed window, we iterate R to our desired right bound, updating the initial count
        then we do a comparison with the target hashmap. (this is an O(1) op as it is capped by the fact that there r only 26 lowercase letters)
        if not, we move L R, updating L R seen 
        return True if dictionaries match
        """
        if len(s1) > len(s2): return False

        print("hi")
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        window_count = {}
        right_bound = len(s1) - 1   

        #initialize initial fixed window
        right = 0
        while right <= right_bound:
            if s2[right] in s1_count:
                window_count[s2[right]] = window_count.get(s2[right], 0) + 1
            right += 1
        if window_count == s1_count: return True

        #reset boundaries
        left = 0
        right = right_bound
        #we shift forward and adjust the count. then we check if it matches. if it does, we return ture
        while right < len(s2) - 1:
            print(window_count, " ", s1_count)
            if s2[left] in s1_count:
                window_count[s2[left]] -= 1
            left += 1
            right += 1
            if s2[right] in s1_count:
                window_count[s2[right]] = window_count.get(s2[right], 0) + 1
            
            if window_count == s1_count: return True

        return False

        




            
            
