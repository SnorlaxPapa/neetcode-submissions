class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False

        def search(parents, word, target_index, position):
            #set up our position and neighbors
            row, col = position
            
            #if our curr element matches, we continue searching its neighbors, else we return
            if board[row][col] != word[target_index]: return

            if target_index == len(word) - 1: 
                nonlocal exists
                exists = True
                return
                
            neighbors = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
            #check through our neighbors for the next word
            parents.add(position)
            for neighbor in neighbors:
                row, col = neighbor
                #check for valid neighbor
                if neighbor in parents or row < 0 or col < 0: continue
                if row == len(board) or col == len(board[0]): continue

                search(parents, word, target_index + 1, neighbor)
            
            parents.discard(position)
        
        #treat each char as beginning
        for row in range(len(board)):
            for col in range(len(board[0])):
                search(set(), word, 0, (row, col))
                if exists == True: return exists

        return False