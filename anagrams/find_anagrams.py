import anagrams.config as config
import pickle
import os 

anagram_map = {}
def load_anagram_map():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        outfile_path = os.path.join(dir_path, config.outfile)
        with open(outfile_path, 'rb') as outfile:
            anagram_map = pickle.load(outfile)
            return anagram_map
    except FileNotFoundError:
        print('No anagrams map found. Call anagrams.generate_anagrams() to create it.')
        exit()

def find_anagrams(word):
    global anagram_map
    if not anagram_map:
        anagram_map = load_anagram_map()
    if not isinstance(word, str):
        raise ValueError('can only find anagrams for strings')
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_map:
        return []
    word_anagrams = anagram_map[sorted_word]
    return word_anagrams
