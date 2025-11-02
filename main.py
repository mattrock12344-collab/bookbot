def get_book_text(book_file_path): 
    # This function reads the content of a book file and returns it as a string.
    with open(book_file_path) as f: 
        book_text = f.read()
    return book_text

def main():
    book_file_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    words = book_text.split()
    print(f"Found {len(words)} total words")

main() 