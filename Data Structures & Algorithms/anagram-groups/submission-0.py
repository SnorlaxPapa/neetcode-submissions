class Solution:
    def checkAnagram(self, str1: str, str2: str):
        """Compares two equal length strings to determine 
        if they are anagrams by comparing count"""
        seen1 = dict.fromkeys(list(str1), 0)
        seen2 = dict.fromkeys(list(str2), 0)

        for index, char in enumerate(str1):
            seen1[char]+=1
            seen2[str2[index]]+=1
        
        for char, count in seen1.items():
            if seen2.get(char) == None:
                return False
            if seen2[char] != count:
                return False

        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """group an array of strings into sublists of anagrams
            1) filter the array of strings based on string length into different buckets with a dict
            2) for each new string seen, we check if it is an anagram with any of the preexisting anagram groups
            3) to reduce number of comparisons we group anagrams according to string length and compare anagrams within that length only
        """
        lenBucket = {}
        
        #O(m) time
        for string in strs:
            length = len(string)
            if lenBucket.get(length) == None:
                #initializes a 2d array containing a unique anagram as an initial group
                lenBucket[length] = [[string]] 
            else:
                #compare to groups of anagram in that specific bucket
                existAnagram = False
                for anagramGroup in lenBucket[length]:
                    #compare with first string in the group
                    if self.checkAnagram(string, anagramGroup[0]) == True:
                        anagramGroup.append(string)
                        existAnagram = True
                        break
                
                if existAnagram == False:
                    lenBucket[length].append([string])

        answers = []
        for values in lenBucket.values():
            for groups in values:
                answers.append(groups)

        return answers
    