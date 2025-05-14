from stats import count_words, count_letters
import sys

def get_book_text(path):
  with open(path) as f:
    contents = f.read()
    return contents
  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  text = get_book_text(sys.argv[1])
  num_words = count_words(text)
  char_list = count_letters(text)

  print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for line in char_list:
    print(f"{line['char']}: {line['num']}")

main()