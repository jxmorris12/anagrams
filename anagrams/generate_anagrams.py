import anagrams.config as config

import os
import pickle

def generate_anagrams():
    words = config.words
    anagram_map = {}

    for word in words:
        sorted_chars = ''.join(sorted(word))
        if sorted_chars not in anagram_map:
            anagram_map[sorted_chars] = []
        anagram_map[sorted_chars].append(word)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    outfile_path = os.path.join(dir_path, config.outfile)
    with open(outfile_path, 'wb') as outfile:
        # Use HIGHEST_PROTOCOL to use the most efficient protocol our version of
        # Pickle knows about
        pickle.dump(anagram_map, outfile, protocol=pickle.HIGHEST_PROTOCOL)
        print('Saved anagrams to {}.'.format(outfile_path))

if __name__ == '__main__': generate_anagrams()
