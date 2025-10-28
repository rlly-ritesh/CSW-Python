# 3. Math Expression Evaluator
# Parse and evaluate expressions like “3 + 5 * 2” without eval().
def evaluateit():
    expression = input("Enter a mathematical expression (e.g., 3 + 5 * 2): ")
    tokens = expression.split()
    
    # Operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    def apply_operator(operators, values):
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            values.append(left / right)
    
    operators = []
    values = []
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isdigit():
            values.append(int(token))
        else:
            while (operators and precedence[operators[-1]] >= precedence[token]):
                apply_operator(operators, values)
            operators.append(token)
        i += 1
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]