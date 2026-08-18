# Day 3 — First Non-Repeating Character

# 🎯 Objective

Solve a string-processing problem that requires finding the first character that appears exactly once in a given string.

The main goal was not only to solve the problem, but also to experiment with different data structures and approaches and evaluate their correctness.

---

# 🧠 Topics

- Strings
- Dictionaries
- Lists
- Loops
- Conditional statements
- Dictionary insertion order
- ```dict.items()```
- ```dict.keys()```
- ```next()```
- ```iter()```
- Algorithmic thinking
- Edge cases
- Choosing appropriate data structures

---

# 💻 Challenge

Create a function called ```first_unique_character()``` that receives a string and returns the first character that appears exactly once.

If there is no unique character, the function should return ```None```.

## Examples

```python
first_unique_character("swiss")
# "w"

first_unique_character("leetcode")
# "l"

first_unique_character("aabbcc")
# None

first_unique_character("a")
# "a"

first_unique_character("")
# None

first_unique_character("aabbc")
# "c"

first_unique_character("programming")
# "p"
```

---

# 🧪 Additional Edge Case

An additional test case was introduced to verify whether an algorithm correctly handles characters that occur more than twice:

```python
first_unique_character("aabcaa")
# "b"
```

This test case was important because it exposed flaws in two alternative approaches.

---

# 1️⃣ Solution 1 — Frequency Dictionary

The first solution counts how many times every character appears.

```python
def first_unique_character(text):
    characters = {}

    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    for char_count in characters.items():
        if char_count[1] == 1:
            return char_count[0]
```

## How it works

The first loop builds a frequency dictionary.

For example:

### "swiss"

```text
s → 3
w → 1
i → 1
```

The second loop then searches the dictionary in insertion order and returns the first character whose frequency is exactly ```1```.

## Result

This solution is correct and handles the tested edge cases.

## Status

✅ Correct

---

# 2️⃣ Solution 2 — List of Unique Characters

The second approach tried to keep only characters that had appeared an odd number of times.

```python
def first_unique_character(text):
    uniques = []

    for char in text:
        if char in uniques:
            uniques.remove(char)
        else:
            uniques.append(char)

    if not uniques:
        return None

    return uniques[0]
```

## Initial reasoning

The idea was:

- If a character appears for the first time, add it.
- If it appears again, remove it.
- The first remaining character should be the first unique character.

This works for many simple cases.

## Problem

The algorithm does not actually track characters that appear exactly once.

Instead, it tracks whether a character has appeared an odd or even number of times.

For example:

```text
1 occurrence → present
2 occurrences → removed
3 occurrences → present again
4 occurrences → removed again
```

Therefore, a character appearing three times could incorrectly be considered unique.

## Status

❌ Incorrect for all possible inputs

## Lesson

A solution can work for several test cases and still be logically incorrect.

Testing edge cases is essential.

---

# 3️⃣ Solution 3 — Dictionary + Deletion

The third approach attempted to apply the same idea using a dictionary instead of a list.

```python
def first_unique_character(text):
    uniques = {}

    for char in text:
        if char in uniques:
            del uniques[char]
        else:
            uniques[char] = 1

    if not uniques:
        return None

    return next(iter(uniques))
```

The expression:

```python
next(iter(uniques))
```

returns the first key in the dictionary.

## Problem

Although the data structure was changed from a list to a dictionary, the underlying algorithmic problem remained.

The dictionary still only tracks whether a character is currently present.

Therefore, characters appearing three or more times can be incorrectly treated as unique.

For example:

```python
first_unique_character("aaabc")
```

should return:

```text
"b"
```

but this approach incorrectly considers ```"a"``` unique after its third occurrence.

# Status

❌ Incorrect for all possible inputs

# Lesson

Changing the data structure does not automatically fix an incorrect algorithm.

The underlying logic must correctly represent the problem being solved.

---

# 🏆 Final Conclusion

The frequency-based dictionary solution is the correct solution among the three approaches.

The main lesson from this challenge was:

```
A solution that works on several examples is not necessarily a correct algorithm.
```

Edge cases can reveal hidden assumptions and logical problems.

The most important edge case in this challenge was a character appearing more than twice. This showed that simply adding and removing characters does not correctly represent the concept of "appears exactly once."

I also learned that choosing a data structure should be based on the operations the problem actually requires.

---

# 💡 What I Learned
- How to count character frequencies using a dictionary.
- How dictionary insertion order can help preserve the order of characters.
- How to iterate through dictionary items.
- How ```next(iter(dictionary))``` can retrieve the first dictionary key.
- Why list membership checks can be inefficient for larger collections.
- Why deleting an item every second time it appears does not track uniqueness correctly.
- Why edge cases are essential when testing algorithms.
- How different data structures can lead to different algorithmic approaches.
- How to question whether a solution is actually correct instead of relying only on basic test cases.

---

# 🧠 Reflection

This challenge was more difficult than the previous two because I experimented with multiple approaches instead of immediately stopping after finding a working solution.

My first solution was correct, but I wanted to find a different and potentially more efficient approach.

The second and third approaches initially seemed promising, but additional edge-case testing revealed that they were tracking odd/even occurrence counts rather than characters that appeared exactly once.

This was a valuable lesson in algorithmic thinking: correctness should be verified against the underlying requirements of the problem, not just a few successful examples.

# ⏱️ Time Spent

Approximately: 1 hour

# ✅ Status

Completed

# Day 3 / 365 🟢