def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

file_contents = main()

def count_words(string):
    word_count = len(string.split())

    return word_count

def count_characters(string):
    char_dict = {}
    lowered_string = string.lower()

    for char in lowered_string:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def dict_to_list(dict):
    char_list = []

    for char, count in dict.items():
        char_count_dict = {"char": char, "count": count}
        char_list.append(char_count_dict)

    return char_list

def sort_on(dict):
    return dict["count"], dict["char"]

char_count_dict = count_characters(file_contents)
char_count_list = dict_to_list(char_count_dict)
char_count_list.sort(reverse=True, key=sort_on)

header = "--- Begin report of books/frankenstein.txt ---"
words_sect = f"{count_words(file_contents)} words found in the document"
footer = "--- End report ---"

print(header + "\n" + words_sect +"\n")

for char_dict in char_count_list:
    character = char_dict["char"]
    count = char_dict["count"]
    if character.isalpha():
        print(f"The \'{character}\' character was found {count} times")

print(footer)
