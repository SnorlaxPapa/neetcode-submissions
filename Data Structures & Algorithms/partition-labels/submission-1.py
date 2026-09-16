class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        if we create a map for all the characters that occur in the string
        e.g.
        xyxxyzbzbbisl
        we can store it in the form char: last_position

        so it would be
        {x: 3, y: 4, z: 7, b: 9, i: 10, s: 11, l: 12}

        then we iterate through the array this time with a right_marker

        while our current position is less than the right_marker, we run through all the char within that range. if it is a different character and its range is > right_marker, we extend it. 
        once we hit the right_market, we append the size of this substring to the group. this is smallest possible substring that contains all of the letters that occur within it. we then set up a new right_marker

        O(n) time, O(m) space where m is num unique characters
        """

        position = {}

        for i, char in enumerate(s):
            position[char] = i

        right_marker = position[s[0]]
        size = 0
        res = []

        for i in range(0, len(s)):
            right_marker = max(right_marker, position[s[i]])
            size += 1

            if i == right_marker:
                res.append(size)

                #reset and move to next group
                size = 0
                if i < len(s) - 1:
                    right_marker = position[s[i + 1]]
                continue


        return res
        