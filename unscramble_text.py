# This is a simple code solution to find a hidden message

# Using the counter from the Python collections since it goes through setting up the counter for you
from collections import Counter

# First let 's open the text file and get a block of scrambled text
with open('scrambled_text.txt') as scrambled_text_from_file:
  scrambled_text_from_file = scrambled_text_from_file.read()
print("Here is the original text:")
print(scrambled_text_from_file)

# Now we sort it out and count the number of times a character shows up
print("Here is a count on how often a character appears: ")
counted_text = Counter(scrambled_text_from_file)
print (counted_text)

# Final result spells keyboarding
