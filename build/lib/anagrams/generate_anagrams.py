import .config
import pickle

words = config.words

anagram_map = {}

for word in words:
    sorted_chars = ''.join(sorted(word))
    if sorted_chars not in anagram_map:
        anagram_map[sorted_chars] = []
    anagram_map[sorted_chars].append(word)

with open(config.outfile, 'wb') as outfile:
    # Use HIGHEST_PROTOCOL to use the most efficient protocol our version of
    # Pickle knows about
    pickle.dump(anagram_map, outfile, protocol=pickle.HIGHEST_PROTOCOL)
