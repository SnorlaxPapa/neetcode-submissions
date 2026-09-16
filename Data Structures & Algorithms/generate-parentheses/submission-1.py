class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []

        def add_bracket(open_count, close_count, prefix):
            #check if we have created a valid string and append if so
            if len(prefix) == 2 * n:
                results.append("".join(prefix))
                return
            
            #we have a guarantee from above that open_count > close_count, so we can search both
            if open_count < n:
                prefix.append("(")
                add_bracket(open_count + 1, close_count, prefix)
                prefix.pop()

            if close_count < open_count:
                prefix.append(")")
                add_bracket(open_count, close_count + 1, prefix)
                prefix.pop()

        add_bracket(0, 0, [])

        return results

