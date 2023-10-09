def validParenthesis(s):
    stack = []
    mapping  = {
        "}":"{",
        ")":"(",
        "]":"["
    }

    for bracket in s:
        if bracket in mapping:
            if stack:
                topElement = stack.pop()
            else:
                return("invalid parenthesis")
            
            if mapping[bracket] != topElement:
                return False
        else:
            stack.append(bracket)

    if len(stack) == 0:
        return("valid parenthesis")
        

inputString = "()[]{[]}()"
print(validParenthesis(inputString))