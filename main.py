from stats import word_count, char_count, sort
import sys

words = word_count()
sorted = sort()
def report():
    print("============ BOOKBOT ============\n"
          "Analyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------\n"
          f"Found {words} total words\n"
          "-------- Character Count -------\n")
    for i in sorted:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

arguments = sys.argv

if len(arguments) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    report()