def is_valid_parentheses(text):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    return not stack 

print(is_valid_parentheses("")) # True
print(is_valid_parentheses("()")) # True
print(is_valid_parentheses("()[]{}")) # True
print(is_valid_parentheses("(]")) # False
print(is_valid_parentheses("([{}])")) # True
print(is_valid_parentheses("([)]")) # False
print(is_valid_parentheses("{[]}")) # True
print(is_valid_parentheses("(")) # False
print(is_valid_parentheses(")")) # False
print(is_valid_parentheses("((()))")) # True
print(is_valid_parentheses("((()")) # False
print(is_valid_parentheses("{[()()]}")) # True