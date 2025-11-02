from stats import word_count, char_count, sort
import sys
arguments = sys.argv
words = word_count()
sorted = sort()
def report():
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {arguments[1]}\n"
          "----------- Word Count ----------\n"
          f"Found {words} total words\n"
          "-------- Character Count -------\n")
    for i in sorted:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
 
report()