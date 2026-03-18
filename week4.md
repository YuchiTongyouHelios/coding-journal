# Week 4: Tooling, Daily Builds, and a Hard Lesson

**March 8 – March 14, 2026**

## What I Built This Week
This week was different – instead of one big project, I focused on **setting up a professional workflow** and **building small daily apps** to lock in Python fundamentals. I also had a reality check about AI.

| Day | Project / Focus | Key Concepts |
|-----|-----------------|--------------|
| 22 | VS Code + Git Setup | Local vs remote, commit, push, source control |
| 23 | Mad Libs Game | Functions, parameters, return, f-strings |
| 24 | Sentence Builder | Lists, loops, `.join()`, `\n`, `len()` |
| 25 | Word Counter | Dictionaries, counting, most common word |
| 26 | AI Violin Coach (with help) | Audio processing, but also **copy‑paste trap** |
| 27 | Tutorial Day | Reflected, planned Month 2 |
| 28 | Month 1 Summary | Wrote `month1.md` |

## What I Learned

### 🛠️ Professional Workflow
- **VS Code needs local files** – GitHub is the cloud backup, not the editor.
- **Git basics**: `add`, `commit`, `push` – and why the commit message matters.
- **Source Control icon** in VS Code shows exactly what’s changed.

### 🐍 Python Drills
- **Lists + loops** = handle any amount of data with few lines.
- **Dictionaries** are perfect for counting – each word maps directly to its count.
- **String methods** `.split()` and `.join()` are super useful.
- **f-strings with conditionals** like `{'s' if count != 1 else ''}`.

### ⚠️ The AI Copy‑Paste Trap
On Day 26 I used AI to generate a complex pitch‑detection program and copy‑pasted it without understanding. It worked, but I felt guilty. So I wrote a **public confession** (`Confession.md`) and promised to never do it again.

**My new rule (the Helios Protocol):**
1. Generate code with AI (if needed).
2. Explain **every line** in my own words.
3. Rewrite it manually in VS Code.
4. Commit only after I truly understand it.

## Code Snippet – Word Counter (Final Version)
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

# Find most common word
most_common = max(word_counts, key=word_counts.get)
print(f"\nMost common word: '{most_common}' ({word_counts[most_common]} times)")
