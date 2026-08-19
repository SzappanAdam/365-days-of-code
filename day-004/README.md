# Day 4 — Two Sum & Time Complexity

# 🎯 Objective

Solve the classic Two Sum problem using different approaches and compare their efficiency.

The main goal was not only to find a correct solution, but also to understand how algorithm choice affects performance.

---

# 🧠 Topics

- Lists
- Dictionaries
- Loops
- Nested loops
- Indexes
- Complement-based problem solving
- Hash maps
- Time complexity
- Big O notation
- Brute force algorithms
- Algorithm optimization

---

# 💻 Challenge

Create a function called ```two_sum()``` that receives:

- a list of integers
- a target integer

The function should return the indexes of two different elements whose sum equals the target.

It can be assumed that exactly one solution exists.

## Example

```python
two_sum([2, 7, 11, 15], 9)
```

Expected result:

```python
[0, 1]
```

Because:

```2 + 7 = 9```

---

# 1️⃣ Dictionary Solution

The first solution uses a dictionary to store information about previously encountered numbers.

```python
def two_sum(numbers, target):
    seen = {}

    for index in range(len(numbers)):
        complement = target - numbers[index]

        if numbers[index] not in seen:
            seen[complement] = index
        else:
            return [seen[numbers[index]], index]
```

## How it works

For every number, the algorithm calculates the value that would be needed to reach the target.

For example:

```python
numbers = [2, 7, 11, 15]
target = 9
```

When processing ```2```:

9 - 2 = 7

The algorithm stores the information that ```7``` is needed.

When it reaches ```7```, it finds that value in the dictionary and returns the two indexes.

## Complexity

Time: ```O(n)``` average case

Space: ```O(n)```

The list is traversed once, while dictionary lookups are approximately ```O(1)``` on average.

---

# 2️⃣ Brute Force Solution

I also implemented a brute force version to compare it with the optimized dictionary approach.

```python
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
```

## How it works

The algorithm checks every possible pair of numbers until it finds the pair whose sum equals the target.

For example:

```python
[2, 7, 11, 15]
```

```text
2 + 7
2 + 11
2 + 15
7 + 11
...
```

The nested loops ensure that every possible pair is checked.

## Complexity

Time: ```O(n²)```

Space: ```O(1)```

The algorithm does not require additional data structures proportional to the input size.

---

## ⚖️ Comparison

Approach	Time Complexity	Space Complexity
Brute Force	```O(n²)```	```O(1)```
Dictionary	```O(n)``` average	```O(n)```

For small inputs, both solutions are extremely fast.

However, as the input size grows, the difference becomes significant.

The brute force solution needs to examine a rapidly increasing number of possible pairs, while the dictionary solution can solve the problem with a single pass through the list.

---

# 💡 What I Learned

- The same problem can have multiple correct solutions.
- A solution being correct does not mean it is optimal.
- Dictionaries can be used to solve lookup problems efficiently.
- A complement can be used to transform the Two Sum problem into a lookup problem.
- Nested loops often lead to ```O(n²)``` time complexity.
- A single loop with efficient dictionary lookups can achieve ```O(n)``` average time complexity.
- Time complexity is an important part of evaluating an algorithm.
- Space complexity is also a trade-off: the faster dictionary solution requires additional memory.

---

# 🧠 Reflection

The brute force solution was surprisingly quick to implement.

The dictionary solution was also straightforward after recognizing that for every number I could calculate the complementary value required to reach the target.

The most important lesson from this challenge was understanding that algorithmic efficiency matters even when multiple solutions produce exactly the same result.

The brute force solution is simpler conceptually, but the dictionary-based solution scales much better for large inputs.

This challenge was my first practical comparison between ```O(n²)``` and ```O(n)``` solutions.

---

# ⏱️ Time Spent

Approximately: 15 minutes

# ✅ Status

Completed

# Day 4 / 365 🟢