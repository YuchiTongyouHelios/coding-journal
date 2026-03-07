# Day 20: File Save Timing – Auto-Save Journal

## What I Built Today
A simple journal program that auto-saves after every entry.

## What I Learned
- **Auto-save** = saves immediately after every change
- Tradeoffs:
  - ✅ Safe – no data lost if program crashes
  - ❌ Slow for large files – saving 1000 entries after every tiny change
- Manual-save would be:
  - ✅ Faster for bulk changes
  - ❌ Risk of losing unsaved work

## My Code (Auto-Save Version)
```python
entries = []

def load():
    global entries
    try:
        with open("journal.txt", "r") as f:
            entries = [line.strip() for line in f]
        print(f"Loaded {len(entries)} entries.")
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        entries = []

def save():
    with open("journal.txt", "w") as f:
        for entry in entries:
            f.write(entry + "\n")
    print("Saved!")

def add_entry(text):
    entries.append(text)
    save()  # Auto-save here
    print("Entry added and saved.")

def show_entries():
    if not entries:
        return "No entries yet."
    result = ""
    for i in range(len(entries)):
        result += f"{i+1}. {entries[i]}\n"
    return result

# Load at start
load()

while True:
    print("\n1. Add entry")
    print("2. View entries")
    print("3. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        text = input("Entry: ")
        add_entry(text)
    elif choice == "2":
        print(show_entries())
    elif choice == "3":
        print("Goodbye!")
        break
```
## Questions & Answers
1. When did it save?
After every single "Add entry" – immediately after appending to the list.

2. If the program crashed right after adding an entry, would you lose it?
No. The save happens right away, so the file is already updated.

3. Is this good or bad for a journal?
Good for a small journal – simple and safe. But for large projects with big files, auto-saving after every change would be too slow. Manual save with a "Save" button would be better.

## What Clicked Today
Save timing is a design decision – there's no single "right way"

Auto-save = safety but slower for big data

Manual-save = faster but risk of losing changes

My To-Do app currently saves after every change (auto-save). For a small to-do list, that's fine
