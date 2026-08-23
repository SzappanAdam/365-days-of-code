# Day 6 — Valid Anagram

## 🎯 Objective

Create a function that determines whether two strings are anagrams of each other.

The main goal was to practice character frequency counting, dictionary-based algorithms, edge-case handling, and improving already-correct code.

## 🧠 Topics

- Strings
- Dictionaries
- Character frequency counting
- Loops
- Dictionary membership
- `any()`
- `dict.values()`
- Early returns
- Time complexity
- Space complexity
- Code simplification
- Pythonic code

---

# 💻 Challenge

Create a function called `is_anagram()` that receives two strings and returns `True` if they contain exactly the same characters with the same frequencies.

The order of the characters does not matter.

If the two strings are not anagrams, the function should return `False`.

## Examples

```python
is_anagram("listen", "silent")
# True

is_anagram("anagram", "nagaram")
# True

is_anagram("rat", "car")
# False

is_anagram("a", "a")
# True

is_anagram("a", "b")
# False

is_anagram("", "")
# True

is_anagram("abc", "ab")
# False

is_anagram("aabbcc", "abcabc")
# True
```

---

# 1️⃣ Solution 1 — Character Frequency Dictionary

My first solution uses a dictionary to count the characters in the first string and then subtracts the occurrences found in the second string.

```python
def is_anagram(text1, text2):
    char_count = {}

    if len(text1) != len(text2):
        return False

    for char in text1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in text2:
        if char in char_count:
            char_count[char] -= 1
        else:
            char_count[char] = -1

    for char in char_count.keys():
        if char_count[char] != 0:
            return False

    return True
```

## 🔎 How it works

First, the lengths of the two strings are compared.

If their lengths are different, they cannot be anagrams.

The first string is then processed and each character is counted.

For example:

```text
"aabbcc"

a → 2
b → 2
c → 2
```

The second string is processed next.

Each occurrence of a character decreases its corresponding count.

If the strings are anagrams, all counts should eventually become zero.

For example:

```text
"aabbcc"
"abcabc"
```

After processing both strings:

```text
a → 0
b → 0
c → 0
```

Therefore, the strings are anagrams.

---

# 2️⃣ Solution 2 — Simplified Final Check

After completing the first solution, I simplified the final dictionary check.

Instead of explicitly looping through every dictionary value:

```python
for char in char_count.keys():
    if char_count[char] != 0:
        return False

return True
```

I used:

```python
return not any(char_count.values())
```

## Final version

```python
def is_anagram(text1, text2):
    char_count = {}

    if len(text1) != len(text2):
        return False

    for char in text1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in text2:
        if char in char_count:
            char_count[char] -= 1
        else:
            char_count[char] = -1

    return not any(char_count.values())
```

## 💡 Why does ```not any()``` work?

```any()``` returns ```True``` if at least one value in the iterable is truthy.

In Python, ```0``` is falsy.

Therefore:

```python
any([0, 0, 0])
```

returns:

```text
False
```

and:

```python
not any([0, 0, 0])
```

returns:

```text
True
```

If any value is non-zero:

```python
any([0, 1, 0])
```

returns:

```text
True
```

and therefore:

```python
not any([0, 1, 0])
```

returns:

```text
False
```

This matches exactly what the algorithm needs.

---

## ⚖️ Complexity

Both versions use the same underlying algorithm.

## Time Complexity

### O(n)

The strings are processed a constant number of times.

## Space Complexity

### O(k)

The dictionary stores the distinct characters.

```k``` represents the number of unique characters.

---

# 🔄 Optimization vs Simplification

The second version is not an algorithmic optimization.

Both versions have the same:

```text
Time:  O(n)
Space: O(k)
```

The improvement is in code readability and conciseness.

The second version expresses the final condition more directly:

"Return ```True``` if none of the character counts are non-zero."

This is a good example of improving code without changing the underlying algorithm.

---

## 🧪 Edge Cases Tested

The following cases were tested:

```python
is_anagram("listen", "silent")
# True

is_anagram("anagram", "nagaram")
# True

is_anagram("rat", "car")
# False

is_anagram("a", "a")
# True

is_anagram("a", "b")
# False

is_anagram("", "")
# True

is_anagram("abc", "ab")
# False

is_anagram("ab", "abc")
# False

is_anagram("aabbcc", "abcabc")
# True
```

The solution correctly handles different string lengths, empty strings, repeated characters, and characters that appear only in one of the strings.

---

# 💡 What I Learned

- How to count character frequencies using a dictionary.
- How dictionaries can be used to compare two collections efficiently.
- How to use a dictionary as a frequency counter.
- Why checking the input lengths first can eliminate impossible cases immediately.
- How ```any()``` works with dictionary values.
- How Python treats ```0``` as a falsy value.
- How to simplify a correct solution without changing its algorithm.
- The difference between algorithmic optimization and code-level simplification.
- How to think about time and space complexity.

---

# 🧠 Reflection

My first approach was somewhat more complicated than necessary, but I was able to independently construct a correct ```O(n)``` solution using a dictionary.

The key idea was to count the characters in the first string and subtract the corresponding counts while processing the second string.

After getting the correct solution, I simplified the final validation using:

```python
not any(char_count.values())
```

This did not improve the algorithmic complexity, but it made the code shorter and more expressive.

This challenge reinforced the idea that a good solution should not only work, but should also be clear and appropriately structured.

---

# ⏱️ Time Spent

Approximately: 40 minutes

# ✅ Status

Completed

# Day 6 / 365 🟢