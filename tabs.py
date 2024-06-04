
def count_text_stats(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_tabs = sum(line.count('\t') for line in lines)
        num_spaces = sum(line.count(' ') for line in lines)
        words = ' '.join(lines).split()
        num_words = len(words)
        num_chars = sum(len(word) for word in words)

    return num_lines, num_tabs, num_spaces, num_words, num_chars

# Example usage
filename = r'C:\Users\RONIT\Desktop\cd\sample.txt'# Change this to your file path
line_count, tab_count, space_count, word_count, char_count = count_text_stats(filename)
print("Number of lines:", line_count)
print("Number of tabs:", tab_count)
print("Number of spaces:", space_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)
