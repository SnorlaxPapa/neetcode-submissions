class TreeNode:
    
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:

    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        
        curr.word = word


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        naive solution: for each word, scan through the entire board. time O(n * m * 3*L) space O(1) n is number of words, m is board size, L is avg length of words
        basically the issue is we have to scan through the entire board each time we want to find a word

        we have a 2d array with characters and we return all words that are present in the grid
        we cannot use the same cell more than once in a word
        to do this, we can use a trie data structure
        we process the board into a trie where for each element, we set it's children to its up/down/left/right depending on where we came from
        the problem is each character can either be the child of another char, or the start of a word, so we need to figure out how to save it as a tree
        for example b can be a continuation of a or could be the start of a new world like back

        instead of processing the board, we can process the words into a trie

        then at each step of the board, we can check if it exists in the tree, returning early if it doesn't exists
        and if we reach the end of a word, we can append that word to the result list. we can use an intermediary temp to keep track of characters accumulated

        Space complexity: O(mL) where m is the number of words and L is the average length of each word
        if each word has different starting letters

        Time complexity O(n * 3^L) where n is the size of the grid and L is the avg length of words
        """

        word_trie = Trie()
        results = set()
        for word in words:
            word_trie.insert(word)
        
        def search(node, parents, pos, string):
            nonlocal board
            nonlocal results
            row, col = pos
            if board[row][col] not in node.children:
                return None
            
            parents.add(pos)
            node = node.children[board[row][col]]
            string += board[row][col]

            if node.word:
                results.add(node.word)

            #search with children
            #need to use a list to maintain the candidate strings. each child can return multiple strings
            if row - 1 >= 0 and (row - 1, col) not in parents:
                search(node, parents, (row - 1, col), string)
            if row + 1 < len(board) and (row + 1, col) not in parents:
                search(node, parents, (row + 1, col), string)
            if col - 1 >= 0 and (row, col - 1) not in parents:
                search(node, parents, (row, col - 1), string)
            if col + 1 < len(board[0]) and (row, col + 1) not in parents:
                search(node, parents, (row, col + 1), string)
            
            parents.remove(pos)
        
        for row in range (len(board)):
            for col in range (len(board[0])):
                if board[row][col] in word_trie.root.children:
                    search(word_trie.root, set(), (row, col), "")

        return list(results)


                    

