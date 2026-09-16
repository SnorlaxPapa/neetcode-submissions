class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        so we are given a string s and t. we are searching for the shortest substring of s that contains every chatacyer in t (i.e. a permutation)
        we can straight away return false if len(t) > len(s)
        
        so we can start off with a hashmap counting the character frequency in the target string t
        if i have a variable length sliding window with L R
        let's say its initial size is len(t) because that's the minimum
        moving R forward is straightforward enough, if my current window does not contain all chaaracters in T, then I must expand
        but what about moving L forward? 
        Why do we move L forward?
        When current window does not contain all characters, a fixed window will shift both L and R.
        However,
        We will not shift L if:
        The next character is a character in t AND that character's count is not in excess (i.e. if we substract it's count, the substring becomes a non-match for that character)
        We will shift L if:
        The next character is not a character in t OR the next character is a character AND its count is in excess

        i.e. we can only afford to shorten the left side if we r not cutting out any important characters

        When we shift L, we will shift it to the next valid character

        if conditions are met, we save this candidaate string and length if they are the min candidates

        this should return us the shortest possible substring
        so if we look at 
        s = "OUZODYXAZV", t = "XYZ"

        we start with
        OUZ -> UZO -> ZOD -> ZODY -> ZODYX (saved, minlength 5) -> ZODYXA -> YXAZ (saved, minlength 4) -> YXAZV

        return YXAZ

        works!!

        ok we also need to define how we match that it contains all the characters 
        custom O(1) 
        we are an expanding window, so once something is matched, it will stay matched as we will not remove the L pointer
        so can create a hashmap called matched_char, 
        then everytime right bumps into a valid char, we check if the counts are equivalent (or greater), then we check if its already matched, if not, we add 1 to our matched_count. save string when matched_count = len(seen_count)
        """

        if len(s) < len(t): return "" 

        left = 0 
        seen_count = {}
        for char in t:
            seen_count[char] = seen_count.get(char, 0) + 1
        
        candidate_string = ""
        min_length = float("inf")
        template_count = {}
        matched_chars = set()
        matched_count = 0
        for right in range(len(s)):
            #check right for valid char
            print(f"right value: {s[right]}")
            if s[right] in seen_count: 
                template_count[s[right]] = template_count.get(s[right], 0) + 1
                if template_count[s[right]] == seen_count[s[right]] and s[right] not in matched_chars:
                    matched_chars.add(s[right])
                    matched_count += 1 

            #we only increment if there is an excess count or its not a valid char
            no_exist = s[left] not in seen_count
            exist_excess = s[left] in seen_count and template_count.get(s[left], 0) >  seen_count[s[left]]
            while no_exist and left < right or exist_excess and left < right:
                print(f"left {left} vlue {s[left]} count: {template_count}")
                if s[left] in seen_count:
                    template_count[s[left]] -= 1
                left += 1
                no_exist = s[left] not in seen_count
                exist_excess = s[left] in seen_count and template_count.get(s[left], 0) >  seen_count[s[left]]
            
            #start of the string should always be a valid character
            while s[left] not in seen_count and left<right:
                left += 1
            
            if matched_count == len(seen_count):
                if (right - left + 1) < min_length:
                    candidate_string = s[left: right+1]
                    min_length = right - left + 1
            print(f"left: {left} right: {right} ", s[left: right+1])
            print(" ")
        return candidate_string
            

                    
                