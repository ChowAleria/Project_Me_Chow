def chow(tokens):
    stack = [[]]
    for token in tokens:
        if token == '(':     # push
            sublist = []
            stack[-1].append(sublist)
            stack.append(sublist)
        elif token == ')':   # pop
            stack.pop()
        else:                # update top of stack
            stack[-1].append(token)
    return stack[0]

stack = ['the', 'cat', 'sat']
stack.append('on')
stack.append('the')
stack.append('mat')
print chow(stack)

stack.pop(0)
stack.pop(0)
print chow(stack)

stack.append('is')
stack.append('the')
stack.append('cat')
print chow(stack)



