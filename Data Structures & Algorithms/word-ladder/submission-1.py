from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)

        def compare(word_one, word_two):
            counter = 0 
            for i in range(len(word_one)):
                if word_one[i] != word_two[i]:
                    counter += 1
                    if counter == 2:
                        return False
            
            return True

        adj_list = {word: [] for word in wordList}
        for primary in range(len(wordList)):
            for comparison in range(primary+1, len(wordList)):
                swappable = compare(wordList[primary], wordList[comparison])
                if swappable == False: continue

                adj_list[wordList[primary]].append(wordList[comparison])
                adj_list[wordList[comparison]].append(wordList[primary])

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            curr_word, count = queue.popleft()

            for swappable in adj_list[curr_word]:
                if swappable in visited: continue
                if swappable == endWord: 
                    return count + 1 
                
                queue.append((swappable, count + 1))
                visited.add(swappable)

        return 0
