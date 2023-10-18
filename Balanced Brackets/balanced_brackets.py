def isBalanced(string):
    stack = []  # created an empty stack to keep track of opening brackets
    bracket = {'{': '}', '(': ')', '[': ']'}  # created a dictionary

# Check if the string length is odd (i.e., an unbalanced number of brackets)
    if len(string) % 2 != 0:
        return 'NO'

# Iterate through each character in the input string.
    for char in string:
        # if the char is an opening bracket add it to the stack
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            # if brackets are present
            if stack:
                top = stack.pop()
                if bracket[top] != char:
                    return 'NO'
            # stack is empty
            else:
                return 'NO'

    return "NO" if stack else "YES"


result = isBalanced("{[()]}")
print(result)
