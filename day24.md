# Day 24: Lists and Loops - Sentence Builder

## What I Built Today
A program that collects any number of words and joins them into a sentence.

## What I Learned
- **Lists** store multiple items in order
- **.append()** adds items to end of list
- **" ".join(list)** combines list into string
- **\n** creates new lines in text
- **len()** counts items in a list

## My Code
```python
print("===Sentence Builder===")
num_words = int(input("How many words do you want in your sentence?"))
words = []
for i in range(num_words):
    word = input(f"word {i+1}: ")
    words.append(word)
sentence = " ".join(words)
print("\n" + "="*40)
print("YOUR SENTENCE")
print(sentence)
print(f"\nStats:")
print(f"- First word: {words[0]}")
print(f"- Last word: {word[-1]}")
print(f"- Total words: {len(words)}")
print("="*40)
```

## Key Takeaway
Lists remember order, loops handle repetition - together they handle any amount of data with few lines.

## What's Next
Ready for more list operations like sorting or counting words.
