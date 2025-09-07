def num_of_words(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
        words = text.split()
        print(f'Found {len(words)} total words')
        
        
def char_count(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
        text = text.lower()
        char_counts = {}
        for char in text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts
    
def sort_words(word_dict):
    return dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

