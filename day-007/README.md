# Day 7 — Contains Duplicate & Weekly Checkpoint

## 🎯 Objective

Determine whether a list contains any duplicate values.

The main challenge was to first create a correct solution and then recognize that the choice of data structure could significantly improve its performance.

This challenge also served as the first weekly checkpoint of the 365-day programming journey.

## 🧠 Topics

- Lists
- Sets
- Membership testing
- Early returns
- Time complexity
- Space complexity
- Algorithm optimization
- Data structure selection
- Weekly review

---

# 💻 Challenge

Create a function called `contains_duplicate()` that returns `True` if a list contains at least one duplicate value.

Otherwise, it should return `False`.

## Examples

```python
contains_duplicate([1, 2, 3, 1])
# True

contains_duplicate([1, 2, 3, 4])
# False

contains_duplicate([1, 1])
# True

contains_duplicate([])
# False

contains_duplicate([5, 5, 5, 5])
# True
```

---

# 1️⃣ Solution 1 — List

My first solution used a list to keep track of previously encountered numbers.

```python
def contains_duplicate(numbers):
    if not numbers:
        return False

    seen = []

    for num in numbers:
        if num in seen:
            return True
        seen.append(num)

    return False
```

## How it works

Each number is checked against the ```seen``` list.

If the number is already present, a duplicate has been found and the function immediately returns ```True```.

Otherwise, the number is added to ```seen```.

If the loop finishes without finding a duplicate, the function returns ```False```.

## Complexity

Time: ```O(n²)``` in the worst case

Space: ```O(n)```

The important issue is the membership check:

```python
num in seen
```

Searching for an element in a list takes ```O(n)``` time in the worst case.

Since this happens for every element, the total time complexity can become ```O(n²)```.

---

# 2️⃣ Solution 2 — Set

After analyzing the first solution, I replaced the list with a set.

```python
def contains_duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True

        seen.add(num)

    return False
```

## How it works

A set is used to store values that have already been encountered.

For each number:

1. Check whether it is already in the set.
2. If it is, return ```True```.
3. Otherwise, add it to the set.
4. Continue until the list has been processed.

The function can stop immediately when a duplicate is found.

---

## ⚖️ Complexity Comparison
Approach	Data Structure	Time	Space
Solution 1	List	```O(n²)``` worst case	```O(n)```
Solution 2	Set	```O(n)``` average	```O(n)```

The second solution is significantly more efficient because set membership testing is ```O(1)``` on average.

The main improvement came from changing the data structure rather than changing the overall algorithmic idea.

---

## 🧠 Key Lesson

One of the most important lessons from this challenge was:

Choosing the right data structure can change the efficiency of an algorithm dramatically.

The two solutions use almost the same overall idea:

```text
Have I seen this number before?
```

The difference is how that question is answered.

### List

```text
Search → O(n)
```

### Set

```text
Search → O(1) average
```

This changes the overall algorithm from approximately:

```text
O(n²)
```

to:

```text
O(n)
```

---

# 📅 Weekly Checkpoint — Days 1–7

The first week focused primarily on fundamental algorithmic thinking and Python data structures.

## Day 1 — Analyze Numbers

Learned to process a collection of numbers and calculate statistics such as:

- minimum
- maximum
- sum
- average
- even count
- frequency

The first introduction to dictionary-based counting.

## Day 2 — Find Duplicates

Practiced detecting repeated values and explored different ways of storing previously encountered elements.

## Day 3 — First Unique Character

Worked with character frequencies and experimented with different data structures.

The main lesson was that changing the data structure can change the way a problem is solved.

## Day 4 — Two Sum

Compared two different approaches:

- brute force
- dictionary-based lookup

This was the first practical comparison between ```O(n²)``` and ```O(n)``` algorithms.

## Day 5 — Valid Palindrome

Learned the two-pointer technique.

Also optimized the initial solution from:

```text
O(n) time
O(n) space
```

to:

```text
O(n) time
O(1) extra space
```

## Day 6 — Valid Anagram

Practiced frequency counting with dictionaries.

Also learned how a correct solution can be simplified using Python's built-in functions such as ```any()```.

## Day 7 — Contains Duplicate

Returned to a familiar problem and solved it again.

The first solution used a list and resulted in ```O(n²)``` worst-case time.

The optimized solution used a set and achieved ```O(n)``` average time.

---

# 📈 What I Learned During Week 1

After the first seven days, several patterns started to become familiar:

## 1. Frequency Counting

Dictionaries can be used to count how often values occur.

```python
frequency[value] = frequency.get(value, 0) + 1
```

## 2. Fast Membership Testing

Different data structures provide different lookup performance.

```text
list → O(n)
set → O(1) average
dict → O(1) average
```

## 3. Two Pointers

Two indexes can move toward each other to solve certain sequence and string problems efficiently.

## 4. Early Returns

If the answer is already known, the function can return immediately instead of processing the remaining input.

## 5. Complexity Matters

A solution that works is not necessarily the best solution.

When the input becomes large, algorithmic complexity can make a huge difference.

## 6. Space Is Also Important

Optimization is not only about runtime.

Sometimes an algorithm can keep the same time complexity while reducing its additional memory usage.

---

# 🧠 Weekly Reflection

The biggest change during the first week was not learning individual Python features.

It was beginning to think about why a particular data structure or algorithm should be used.

At the beginning of the week, the main question was:

```"Can I solve this problem?"```

By the end of the week, a new question started to appear:

```"Can I solve this problem efficiently?"```

The ```contains_duplicate()``` challenge demonstrated this especially well.

The first solution was correct, but after analyzing its complexity, I was able to independently recognize that a set would provide much faster membership checks.

This is an important step toward developing stronger algorithmic thinking.

---

# 🚀 Next Steps

The first week focused mainly on:

```text
Python fundamentals
        ↓
Data structures
        ↓
Lookup techniques
        ↓
Basic algorithms
        ↓
Time & Space Complexity
```

The next stage will gradually introduce more algorithmic patterns and more challenging problems.

The goal is not simply to solve more problems, but to become better at recognizing which approach and data structure fit a given problem.

---

# ⏱️ Time Spent

Approximately: 5 hours across the week

# 📊 Progress

7 / 365 days completed

# Week 1 / 52+ 🟢

---

# 🏆 Week 1 Complete

The first week of the 365-day programming journey is complete.

# 7 days down. 358 to go. 🚀