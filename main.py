import stats
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
         
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    stats.num_of_words(f'/home/spreddy/codespace/bookbot/{sys.argv[1]}')
    counts = (stats.char_count(f'/home/spreddy/codespace/bookbot/{sys.argv[1]}'))
    print("------- Character Count ---------")
    sorted_counts = stats.sort_words(counts)
    for char, count in sorted_counts.items():
        if char.isalpha():
            print(f'{char}: {count}') 
    print("============= END ===============")
    

main()
