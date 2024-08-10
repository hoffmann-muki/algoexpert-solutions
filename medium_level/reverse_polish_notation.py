# O(n) time | O(n) space
def reversePolishNotation(tokens):
    stack = []
    for token in tokens:
        if not isOperator(token):
            stack.append(int(token))
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(compute(a, token, b))
    return stack.pop()

def isOperator(letter):
    return letter == '*' or letter == '/' or letter == '+' or letter == '-'

def compute(a, operator, b):
    if operator == '*':
        return a * b
    elif operator == '/':
        if b < 0:
            if a < 0:
                return -a // -b
            return -(a // -b)
        else:
            if a < 0:
                return -(-a // b)
            return a // b
    elif operator == '+':
        return a + b
    elif operator == '-':
        return a - b
