def newStack():
    stack = []
    return stack

def isEmpty(stack): # checking if the stack is empty
    return len(stack) == 0


# adding elements
def push(stack,item):
    stack.append(item)

# popping elements
def pop(stack):
    if isEmpty(stack):
        return("nothing to pop")
    else:
        stack.pop()

stack = newStack()
push(stack, "SR")
push(stack, "AS")
push(stack, "MC")
push(stack, "PNM")
push(stack, "SR")
push(stack, "RP")
push(stack, "SR")
pop(stack)
push(stack, "AS")
print(stack)
