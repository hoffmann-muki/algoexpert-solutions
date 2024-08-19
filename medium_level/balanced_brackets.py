bracketMap = { '}':'{', ')':'(', ']':'[' }

# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    for letter in string:
        if isOpeningBracket(letter):
            stack.append(letter)
        elif isClosingBracket(letter):
            n = len(stack)
            foundMatchingBracket = False
            while n > 0:
                element = stack.pop()
                if element == openingBracketFor(letter):
                    foundMatchingBracket = True
                    break
                else:
                    return False
            if not foundMatchingBracket:
                return False
        else:
            continue
    return len(stack) == 0

def isOpeningBracket(letter):    
    return letter == '(' or letter == '[' or letter == '{'

def isClosingBracket(letter):
    return letter == ')' or letter == ']' or letter == '}'

def isOptionalCharacter(letter):
    return not isOpeningBracket(letter) and not isClosingBracket(letter)

def openingBracketFor(letter):
    global bracketMap
    return bracketMap[letter]
