import re

def count_chars_and_words(text):
    char_count = len(text)
    word_count = len(re.findall(r'\b\w+\b', text))
    return char_count, word_count

def process_file(filename):
    char_count = 0
    word_count = 0
    line_count = 0

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            line_count += 1
            line = re.sub(r'abc', 'ABC', line)
            print(line, end='')
            chars, words = count_chars_and_words(line)
            char_count += chars
            word_count += words

    print(f"\nCharacters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")

if __name__ == "__main__":
    filename = 'C:\\Users\\RONIT\\Desktop\\cd\\sample.txt'  # Define the file path here
    process_file(filename)
