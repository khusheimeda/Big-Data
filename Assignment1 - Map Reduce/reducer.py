#!/usr/bin/python3
import sys

# current_word will be used to keep track of either recognized or unrecognized tuples
current_word = None
# current_count will contain the number of tuples of word = current_word seen till now
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    word,count = line.split("\t")
    count = int(count)
    # If the seen word is equal to the one we're counting, update count
    if (current_word == word):
        current_count += count
    else:
        if current_word:
            print(current_count)
        # This is a new word, so initialise current_word and current_count variables 
        current_count = count
        current_word = word
if current_word == word:
    print(current_count)

        
