# 🧠 Binary Search in Python

This is a **simple implementation of the binary search algorithm** in Python. It demonstrates how to search for a target item inside a **sorted list of strings** using recursion.

---

## 🔍 Features

- Recursive binary search function
- Works with both integer and string lists
- Interactive user input for target search
- Case-insensitive string comparison

---

## 🧪 How It Works

1. The list of strings is sorted alphabetically (case-insensitive).
2. The user enters a word to search.
3. The program applies binary search to locate the item and displays its index (or `Not found` if it doesn’t exist).

---

## 📦 Example

```python
val_str = ['apple','ball','egg','ice','nice']
# After sorting: ['apple', 'ball', 'egg', 'ice', 'nice']
target = 'ice'
# Output: The target is at index: 3