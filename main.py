def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
     with open(path) as f:
          return f.read()

def get_character_count(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

def sort_on(dict):
     return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

               

main()

