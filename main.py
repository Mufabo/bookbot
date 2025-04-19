from stats import get_num_words, get_num_characters, sort_chars
import sys

def get_book_test(file_path: str) -> str:
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    file_path =  sys.argv[1]
    txt = get_book_test(file_path)
    num_words = get_num_words(txt)
    chars = get_num_characters(txt)
    sorted_chars = sort_chars(chars)
    print(f"""============ BOOKBOT ============
    Analyzing book found at {file_path}...
    ----------- Word Count ----------
    Found {get_num_words(txt)} total words
    --------- Character Count -------
    """)
    for i in sorted_chars:
      if i["char"].isalpha():
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")


if __name__ == "__main__":
  main()
