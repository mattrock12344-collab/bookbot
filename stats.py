import sys
arguments = sys.argv
if len(arguments) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_file_path): 
    # This function reads the content of a book file and returns it as a string.
    with open(book_file_path) as f: 
        book_text = f.read()
    return book_text

def sort_on(items):
    return items["num"]

def word_count():
    book_file_path = arguments[1]
    book_text = get_book_text(book_file_path)
    words = book_text.split()
    return len(words)

def char_count():
    book_file_path = arguments[1]
    book_text = get_book_text(book_file_path)
    lower = book_text.lower()
    char = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'â': 0,
            'ê': 0, 'ë': 0, 'ô': 0}
    for i in lower:
        if i in char:
            char[i] += 1
    return char

def sort():
    sorted = []
    char = char_count()
    for i in char:
        sorted.append({"char": i, "num": char[i]})
    sorted.sort(key=sort_on, reverse=True)
    return sorted
    