from stats import count_words, times_char, sort_dictionary
import sys
def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
        return file_contents 
def main():
    numb = len(sys.argv)
    if(numb != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_words = get_book_text(sys.argv[1])
    totalwords = count_words(book_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {totalwords} total words")
    print("--------- Character Count -------")
    char_count = times_char(book_words)
    sorted_char = sort_dictionary(char_count)
    for x in sorted_char:
        if x["char"].isalpha():
            print(f"{x['char']}: {x['num']}")
    print("============= END ===============")

main()