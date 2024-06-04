import re

def append_counter(word, count):
    return f"{word}{count}"

def process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    vowel_count = 0
    total_words = 0

    def replace_word(match):
        nonlocal vowel_count, total_words
        word = match.group(0)
        if re.match(r'^[aeiouAEIOU]', word):
            vowel_count += 1
            word = append_counter(word, vowel_count)
        total_words += 1
        return word

    processed_content = re.sub(r'\b[a-zA-Z]+\b', replace_word, content)

    print(processed_content)
    print(f"\nTotal words: {total_words}")

if __name__ == "__main__":
    filename = 'C:\\Users\\RONIT\\Desktop\\cd\\sample.txt'
    process_file(filename)
