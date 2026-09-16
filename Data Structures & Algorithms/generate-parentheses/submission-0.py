class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []

        def add_bracket(open_count, close_count, prefix):
            #check if we have created a valid string and append if so
            if len(prefix) == 2 * n:
                results.append("".join(prefix))
                return 
            
            #if our counts are equal, can only add open. need to handle edge case where its the last bracket
            if open_count == close_count and len(prefix) != 2*n - 1:
                if len(prefix) == 2 * n - 1: return

                prefix.append("(")
                add_bracket(open_count + 1, close_count, prefix)
                prefix.pop()
                return
            
            #we have a guarantee from above that open_count > close_count, so we can search both
            if open_count < n:
                prefix.append("(")
                add_bracket(open_count + 1, close_count, prefix)
                prefix.pop()
    
            prefix.append(")")
            add_bracket(open_count, close_count + 1, prefix)
            prefix.pop()

        add_bracket(0, 0, [])

        return results

