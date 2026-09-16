import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        RPN -> grabs last two numbers and performs operation

        operate assuming input is syntatically correct
        let us assume program will not pass us 0/0 or an invalid arithmetic expression as specified in the qn

        so we iterate down the tokens, continue if its NaN
        we maintain a stack tracking current result tempResult = []
        when we hit an operator, we take the last two numbers in the result
        """

        tempResult = []
        operations = {
                        "+": lambda x, y: x + y,
                        "-": lambda x, y: x - y,
                        "/": lambda x, y: math.trunc(x / y),
                        "*": lambda x, y : x * y
                     }
        
        for index, token in enumerate(tokens):
            if token in operations:
                result = operations[token](tempResult[-2], tempResult[-1])
                tempResult.pop()
                tempResult.pop()
                tempResult.append(int(result))
            else:
                tempResult.append(int(token))
        
        return tempResult[0]