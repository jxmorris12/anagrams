## anagrams

### Usage
This package provides an easy way to find anagrams for a given English word in Python 3.

```
>>> from anagrams import find_anagrams
>>> find_anagrams('stale')
['least', 'setal', 'slate', 'stale', 'steal', 'stela', 'tales']
```


### Corpus

This is based on the corpus of words provided by NLTK. You can re-run the code using your own corpus of words from any language. Edit the `words` variable in `config.py` to a different list of words (they must be strings). Then re-run `generate-anagrams.py` to generate a new map of anagrams. `english_anagrams.py` will use the new map by default.
