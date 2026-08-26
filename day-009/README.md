# Day 9 — Longest Consecutive Sequence

## 🎯 Objective

Create a function that finds the length of the longest sequence of consecutive integers in a list.

The order of the input numbers does not matter, and duplicate values should not affect the result.

The main goal was to first create a correct solution and then optimize it by eliminating the need for sorting.

## 🧠 Topics

- Lists
- Sets
- Sorting
- Membership testing
- Loops
- `while` loops
- Algorithm optimization
- Time complexity
- Space complexity
- Identifying sequence starting points

---

# 💻 Challenge

Create a function called `longest_consecutive()` that returns the length of the longest sequence of consecutive integers.

## Examples

```python
longest_consecutive([100, 4, 200, 1, 3, 2])
# 4
```

The longest sequence is:

```text
1 → 2 → 3 → 4
```

Another example:

```python
longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# 9
```

The longest sequence is:

```text
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
```

---

# 🧪 Test Cases

```python
longest_consecutive([100, 4, 200, 1, 3, 2])
# 4

longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# 9

longest_consecutive([1, 2, 3, 4, 5])
# 5

longest_consecutive([5])
# 1

longest_consecutive([])
# 0

longest_consecutive([10, 5, 20, 15])
# 1

longest_consecutive([1, 2, 2, 3])
# 3

longest_consecutive([-2, -1, 0, 1, 2])
# 5
```

---

# 1️⃣ Solution 1 — Sorting

My first solution removes duplicates and sorts the numbers:

```python
def longest_consecutive(numbers):
    numbers = sorted(set(numbers))

    if not numbers:
        return 0

    current_length = 1
    longest_length = 1

    for i in range(len(numbers) - 1):
        if numbers[i] + 1 == numbers[i + 1]:
            current_length += 1
        else:
            current_length = 1

        if current_length > longest_length:
            longest_length = current_length

    return longest_length
```

## 🔎 How it works

First, the input is converted into a set:

```python
set(numbers)
```

This removes duplicate values.

The set is then sorted:

```python
sorted(set(numbers))
```

After sorting, consecutive numbers appear next to each other.

For example:

```text
[100, 4, 200, 1, 3, 2]
```

becomes:

```text
[1, 2, 3, 4, 100, 200]
```

The algorithm then checks neighboring elements.

If the next number is exactly one greater than the current number, the current sequence continues.

Otherwise, the current sequence starts over.

---

## ⚖️ Complexity — Solution 1

`Time Complexity`

```O(n log n)```

Removing duplicates takes approximately ```O(n)``` on average, but sorting requires ```O(n log n)``` time.

Therefore, sorting dominates the overall complexity.

`Space Complexity`

```O(n)```

A set and sorted list are created from the input.

---

# 2️⃣ Solution 2 — Set-Based Optimization

The second solution eliminates sorting completely.

```python
def longest_consecutive(numbers):
    seen = set(numbers)

    if not seen:
        return 0

    current_number = 0
    current_length = 0
    longest_length = 0

    for x in seen:
        if x - 1 not in seen:
            current_number = x
            current_length = 1

        while current_number + 1 in seen:
            current_number += 1
            current_length += 1

        if current_length > longest_length:
            longest_length = current_length

    return longest_length
```

---

## 🔎 How the Optimized Solution Works

The key idea is to store all numbers in a set:

```python
seen = set(numbers)
```

This provides fast membership testing.

The algorithm then checks whether the current number is the `start of a sequence`.

A number ```x``` is a sequence starting point if:

```python
x - 1 not in seen
```

For example:

```text
1 → 2 → 3 → 4
```

For ```1```:

```text
1 - 1 = 0
```

If ```0``` is not in the set, ```1``` is a starting point.

The algorithm then checks:

```text
2?
3?
4?
5?
...
```

using:

```python
while current_number + 1 in seen:
```

This counts the entire consecutive sequence.

---

## 🧠 Why Check Only Sequence Starting Points?

Consider:

```text
1, 2, 3, 4
```

The number ```1``` is a starting point because ```0``` does not exist.

However:

```text
2 - 1 = 1
```

and ```1``` exists.

Therefore, ```2``` is not a starting point.

The same is true for ```3``` and ```4```.

This prevents the algorithm from repeatedly scanning the same sequence.

---

# 📊 Complexity Comparison
Approach	Main Technique	Time	Space
Solution 1	Sort + scan	```O(n log n)```	```O(n)```
Solution 2	Set + sequence starts	```O(n)``` average	```O(n)```

The optimized version removes the sorting step and uses constant-time average membership checks instead.

---

## 🚀 Optimization

The first solution was already correct, but it relied on sorting:

```python
sorted(set(numbers))
```

Sorting introduced an ```O(n log n)``` component.

The optimized solution instead uses a set and asks:

Is this number the beginning of a consecutive sequence?

Only numbers that are sequence starting points are expanded.

This allows the algorithm to achieve:

```text
O(n)
```

average time complexity.

---

# 🧠 Key Lesson

The biggest lesson from this challenge was learning that sorting is not always necessary.

A problem may appear to require the data to be ordered, but sometimes the same information can be obtained more efficiently through a different data structure.

In this case, a set allows fast membership testing:

```python
x in seen
```

and:

```python
x not in seen
```

This makes it possible to identify sequence starting points without sorting the entire collection.

---

# 🔥 Connection to Previous Days

This challenge builds directly on ideas from earlier days.

`Day 2 — Find Duplicates`

I first worked with dictionaries to track values.

`Day 7 — Contains Duplicate`

I learned that replacing a list with a set can improve membership testing from:

```text
O(n)
```

to:

```text
O(1) average
```

`Day 9 — Longest Consecutive Sequence`

I applied the same idea to a more complex problem.

Instead of using a set only to detect duplicates, I used it to determine whether consecutive numbers exist.

This was the first time I independently recognized that a set could eliminate the need for sorting.

---

# 💡 What I Learned
- How to remove duplicates with a set.
- How sorting affects algorithm complexity.
- How to use fast membership testing.
- How to identify the beginning of a consecutive sequence.
- How a ```while``` loop can expand a sequence.
- Why checking only sequence starting points prevents unnecessary work.
- How changing the algorithm can improve ```O(n log n)``` to ```O(n)```.
- How previous knowledge about data structures can be applied to new problems.

---

# 🧠 Reflection

My first solution used:

```python
sorted(set(numbers))
```

which made the problem straightforward because consecutive numbers could simply be compared next to each other.

After analyzing the complexity, I realized that sorting was the expensive part.

I then created a second solution using a set without sorting.

The key idea was to recognize that a number only needs to start a sequence if its previous number does not exist.

For example:

```text
1 → 2 → 3 → 4
↑
sequence starts here
```

but ```2```, ```3```, and ```4``` do not start new sequences.

The optimized solution therefore avoids unnecessary work and achieves ```O(n)``` average time complexity.

This challenge was a good example of how choosing the right data structure can lead to a fundamentally better algorithm.

---

# ⏱️ Time Spent

Approximately: 45 minutes

# 📊 Progress

`9 / 365 days completed`

`Week 2 — Day 9 🟢`

# 🏆 Day 9 Complete

Successfully implemented two solutions:

```text
Solution 1 → O(n log n)
Solution 2 → O(n) average
```

The second solution eliminates sorting and uses a set to efficiently identify consecutive sequences.

# Day 9 / 365 🟢