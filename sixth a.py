# Function to define precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0

# Function to convert infix to postfix
def infix_to_postfix(exp):
    stack = []
    postfix = ""

    for ch in exp:
        if ch.isalnum():          # Operand
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:                     # Operator
            while stack and precedence(ch) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

# Main Program
exp = input("Enter Infix Expression: ")
result = infix_to_postfix(exp)
print("Postfix Expression:", result)
