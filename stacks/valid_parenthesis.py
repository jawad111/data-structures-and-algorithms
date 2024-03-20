'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''
def valid(s):
    if(len(s) == 0):
        return False
    stack = []
    stackIndex = -1
    for char in s:
        if(char == "(" or char == "[" or char == "{"):
            stack.append(char)
            stackIndex +=1 
        elif(char == ")" or char == "]" or char == "}"):
            top = stack[stackIndex]
            print(top, char, stackIndex, stack)

            if((char == ")" and top == "(") or (char == "]" and top == "[") or (char == "}" and top == "{")):
                stack.pop()
                stackIndex -=1
            elif((char == ")" and top != "(") or (char == "]" and top != "[") or (char == "}" and top != "{")):
                return False
        
    if(len(stack) == 0):
        return True
    return False


print(valid("{[]}"))


