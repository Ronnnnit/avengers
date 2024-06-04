import re

def lexical_analyzer(input_text):
    tokens = []
    current_token = ''
    in_comment = False

    # Regular expressions for tokens
    identifier_regex = r'[a-zA-Z][a-zA-Z0-9]*'
    number_regex = r'\d+'
    symbol_regex = r'[\[\]()+\-*/=]'

    for line in input_text.split('\n'):
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Remove comments
        line = re.sub(r'#.*', '', line)

        # Split line into tokens
        for token in re.findall(f'{identifier_regex}|{number_regex}|{symbol_regex}', line):
            tokens.append(token)

    return tokens

if __name__ == "__main__":
    # Example input text
    input_text = """
    # This is a comment
    x = 10
    y = 20
    result = x + y
    """

    tokens = lexical_analyzer(input_text)
    print("Tokens:", tokens)
