class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            joins a list of strings into one string
            characters are ASCII-256
            considerations: characters can be any ASCII-256 valid character
            cannot simply pass in raw strings with split or join as string could be whitespace or multiple words
            could embed key at the end signifiying the length of each string
            add key at the end in format 5133 where each number indicates the length of each string. passed to machine 2
            key prefix whitespace to indicate start of key
            cause string length > 10, we add , delimiter
        """

        if strs == []:
            return ""

        passedString = "".join(strs)

        key = " "
        for string in strs:
            key+=str(len(string))
            key+=","
        
        passedString = passedString + key[:-1]
        return passedString



    def decode(self, s: str) -> List[str]:
        """
            extract the key 
            parse
        """
        if s == "":
            return []

        key = s.split(" ")[-1].split(",")
        results = []
        index = 0
        # O(n) 
        for length in key:
            endStr = index + int(length) 
            results.append(s[index:endStr])
            index = endStr
        
        return results

