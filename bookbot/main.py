def get_book_content(path):
    with open(path) as book:
        return book.read()

def get_char_count(text):
    result = {}
    for char in text:
        try:
            result[char.lower()] += 1
        except KeyError:
            result[char.lower()] = 1

    return result

def sorted_char_occurrences(text):
    char_list = []
    chars = get_char_count(text)

    for char in chars:
        if char.isalpha():
            char_list.append({
                "char": char,
                "occurrence": chars[char]
            })

    return sorted(char_list, reverse=True, key=lambda dict: dict["occurrence"])

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_content(book_path)
    num_of_words = len(text.split())

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document\n")

    for each in sorted_char_occurrences(text):
        print(f"Character {each["char"]} occurred {each["occurrence"]} times")

    print("\n--- Emd of report ---")

main()
