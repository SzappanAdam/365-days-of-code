# Day 5 — Valid Palindrome

## 🎯 Objective

Create a function that determines whether a given text is a palindrome.

The function should ignore:

- spaces
- punctuation
- capitalization

The main goal of this challenge was to practice the two-pointer technique and then optimize the initial solution by reducing unnecessary memory usage.

## 🧠 Topics

- Strings
- String methods
- `isalnum()`
- `lower()`
- Two-pointer technique
- `while` loops
- Input preprocessing
- Time complexity
- Space complexity
- Algorithm optimization

---

# 💻 Challenge

Create a function called `is_palindrome()` that returns `True` if the given text is a palindrome and `False` otherwise.

The function should ignore spaces, punctuation, and capitalization.

## Examples

```python
is_palindrome("racecar")
# True

is_palindrome("hello")
# False

is_palindrome("A man, a plan, a canal: Panama")
# True

is_palindrome("Was it a car or a cat I saw?")
# True

is_palindrome("Python")
# False

is_palindrome("")
# True

is_palindrome("a")
# True
```

---

# 1️⃣ Solution 1 — Cleaned String + Two Pointers

The first solution creates a new string containing only alphanumeric characters.

```python
def is_palindrome(text):
    clean = ""

    if not text:
        return True

    for char in text:
        if char.isalnum():
            clean += char

    clean = clean.lower()

    i = 0
    j = len(clean) - 1

    while i < j:
        if clean[i] != clean[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
```

## How it works

First, the original text is cleaned by removing all characters that are not alphanumeric.

The cleaned string is then converted to lowercase.

After that, two pointers are used:

- ```i``` starts at the beginning
- ```j``` starts at the end

The characters at both positions are compared while the pointers move toward the center.

If two characters are different, the function immediately returns ```False```.

If all relevant characters match, the function returns ```True```.

## Complexity

Time: ```O(n)```

Space: ```O(n)```

The algorithm requires additional memory for the cleaned string.

---

# 2️⃣ Solution 2 — Two Pointers Without Creating a New String

The second solution improves the first approach by eliminating the need to create a separate cleaned string.

```python
def is_palindrome(text):
    if not text:
        return True

    text = text.lower()

    i = 0
    j = len(text) - 1

    while i < j:
        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        elif text[i] != text[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
```

## How it works

Instead of creating a separate cleaned string, the algorithm works directly on the original text.

The two pointers start at opposite ends of the string.

If the left pointer encounters a non-alphanumeric character, it moves forward.

If the right pointer encounters a non-alphanumeric character, it moves backward.

Only relevant characters are compared.

This allows the algorithm to perform the palindrome check without creating an additional string.

---

## ⚖️ Comparison
Approach	Time Complexity	Space Complexity
Cleaned String	```O(n)```	```O(n)```
Direct Two Pointers	```O(n)```	```O(1)```

Both approaches have the same asymptotic time complexity.

The important improvement is the space complexity.

The first solution creates a new string whose size can grow with the input.

The second solution uses only a few variables and works directly with the original string.

Therefore, the second approach is more memory-efficient.

---

# 💡 What I Learned

- How to use the two-pointer technique.
- How to compare elements from opposite ends of a sequence.
- How ```isalnum()``` can be used to identify relevant characters.
- How ```lower()``` can normalize text for case-insensitive comparisons.
- How to ignore irrelevant characters without creating a new data structure.
- The difference between time complexity and space complexity.
- How two algorithms can both have ```O(n)``` time complexity while having different memory requirements.
- How to optimize an existing solution without changing its fundamental algorithm.

---

# 🧠 Reflection

My first solution was already correct, but it created a separate cleaned string before performing the palindrome check.

I then tried to improve the solution by asking whether the extra string was actually necessary.

The second approach uses two pointers directly on the original string and skips irrelevant characters as they are encountered.

This reduced the additional space requirement from ```O(n)``` to ```O(1)``` while keeping the time complexity at ```O(n)```.

The most important lesson from this challenge was that optimization is not always about reducing runtime. Memory usage can also be optimized.

---

# ⏱️ Time Spent

Approximately: 1,5 hour

# ✅ Status

Completed

# Day 5 / 365 🟢