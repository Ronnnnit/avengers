def count_chars_and_words(text):
    char_count = len(text)
    word_count = len(text.split())
    return char_count, word_count

def process_file(input_filename, output_filename):
    char_count = 0
    word_count = 0
    line_count = 0

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())

            # Write line number and content to output file
            output_file.write(f"{line_count}: {line}")

    return char_count, word_count, line_count

if __name__ == "__main__":
    input_filename = 'input.txt'   # Provide the input file path
    output_filename = 'output.txt' # Provide the output file path

    char_count, word_count, line_count = process_file(input_filename, output_filename)

    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")
