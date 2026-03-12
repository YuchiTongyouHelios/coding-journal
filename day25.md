# Day 25: Word Counter with Dictionaries

## What I Built Today
A program that counts how many times each word appears in a sentence.

## What I Learned
- **Dictionaries** store word-count pairs
- **word_counts[word] = 1** creates/updates entries
- **Indentation matters** - everything inside loop must be indented
- **f-strings with conditionals** like `{'s' if count != 1 else ''}`

## My Code
```python
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
print(f"Word Count: {len(words)}")
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f"Unique words: {len(word_counts)}")
print("\nWord Frequencies:")
for word in word_counts:
    count = word_counts[word]
    print(f"- {word}: {count} time{'s' if count != 1 else ''}")
most_common_word = ""
highest_count = 0
for word in word_counts:
    if word_counts[word] > highest_count:
        highest_count = word_counts[word]
        most_common_word = word
print(f"\n Most common word: '{most_common_word}' ({highest_count} times)")
```

## Key Takeaway
Dictionaries are perfect for counting - each word maps directly to its count.

## What's Next
Ready for more challenges!
