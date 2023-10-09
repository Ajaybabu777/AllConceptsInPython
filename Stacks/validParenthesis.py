def validParenthesis(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()","").replace("[]","").replace("{}","")
        
    if len(s) == 0:
        return("valid parenthesis")
    else:
        return("invalid parenthesis")
        

inputString = "()[]{[]}"
print(validParenthesis(inputString))