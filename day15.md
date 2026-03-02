# Day 15: Index Owning – Drilling the Basics

## What I Built Today
- `explain_index()` function that shows how indexes map to positions
- Finally understood the math behind negative indexes

## What I Learned
- Indexes are positions, starting at 0
- `len()` gives total items, last index is always `len-1`
- Negative indexes count from the end (-1 is last)
- Formula: `negative_index + len(list) = positive_index`
- Functions can take lists as parameters (`lst`)

## One Thing I Struggled With
- Kept mixing up the list itself with the index number
- Had to slow down and understand that `real_position` is just a number
- Realized I was guessing instead of thinking

## My Code (End of Day 15)
```python
def explain_index(lst, idx):
    if idx >= 0:
        real_position = idx
    else:
        real_position = len(lst) + idx
    
    item = lst[real_position]
    print(f"Index {idx} maps to position {real_position} which contains {item}")

# Testing it out
my_list = [10, 20, 30, 40, 50]
explain_index(my_list, 2)   # Should show position 2 = 30
explain_index(my_list, -1)   # Should show position 4 = 50
explain_index(my_list, -3)   # Should show position 2 = 30
