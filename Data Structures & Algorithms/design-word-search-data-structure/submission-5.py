class DictionaryNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = DictionaryNode()

    def addWord(self, word: str) -> None:
        #use a trielike system to add words
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = DictionaryNode()
            curr = curr.children[char]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
    
        def dfs(root, word):
            curr = root
            print(curr.children.keys(), word)
            for index, char in enumerate(word):
                if char == ".":
                    for child in curr.children:
                        if dfs(curr.children[child], word[index + 1:]) == True:
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

            return curr.is_end

        return dfs(self.root, word)

                    
        
