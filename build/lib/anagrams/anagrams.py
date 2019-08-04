import .config as config
import pickle
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
outfile_path = os.path.join(dir_path, config.outfile)
with open(outfile_path, 'rb') as outfile:
    anagram_map = pickle.load(outfile)

def anagrams(word):
    if not isinstance(word, str):
        raise ValueError('can only find anagrams for strings')
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_map:
        return []
    word_anagrams = anagram_map[sorted_word]
    return word_anagrams
