def is_balanced_delimiters(string):
    stack = []
    opening_delimiters = ['(', '[', '{']
    closing_delimiters = [')', ']', '}']
    
    for char in string:
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack:
                return False
            top = stack.pop()
            if opening_delimiters.index(top) != closing_delimiters.index(char):
                return False
    
    return len(stack) == 0


# Interactive user input
print("Balanced Delimiters Program")
print("Enter a string to check if it has balanced delimiters:")
user_input = input()

result = is_balanced_delimiters(user_input)
if result:
    print("The string has balanced delimiters.")
else:
    print("The string does not have balanced delimiters.")
