from collections import Counter

#sample text
text = """
Python is an amazing programming language. Python is fun to learn and powerful to use.
"""

#split text into words and count frequency
words =  text.lower().split()
word_count = Counter(words)

#display word frequencies
print("World Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")