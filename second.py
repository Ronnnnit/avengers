def compile(expression):
    # Ensure the expression is properly formatted as a string
    return ''.join(expression.split())

# Example usage
expression = "3 + 4 * 2"
generated_code = compile(expression)
print("Generated Python code:", generated_code)

# Evaluate the generated code
result = eval(generated_code)
print("Result of expression:", result)
