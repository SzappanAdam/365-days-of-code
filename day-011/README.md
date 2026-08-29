# Day 11 — Move Zeroes

## 🎯 Objective

Create a function that moves all zeroes in a list to the end while maintaining the relative order of the non-zero elements.

The challenge was solved in two different ways:

1. A straightforward solution using an additional list.
2. An optimized **in-place** solution using `O(1)` extra space.

The main goal was to understand how the same `O(n)` time complexity can be achieved with significantly different memory usage.

---

## 🧠 Topics

* Lists
* Loops
* `for` loops
* `while` loops
* In-place modification
* Two-pointer-style technique
* Space complexity
* Time complexity
* Preserving element order

---

# 💻 Challenge

Create a function called `move_zeroes()` that moves every `0` to the end of the list.

The relative order of all non-zero elements must remain unchanged.

### Example

```python
move_zeroes([0, 1, 0, 3, 12])
# [1, 3, 12, 0, 0]
```

Another example:

```python
move_zeroes([1, 0, 2, 0, 3])
# [1, 2, 3, 0, 0]
```

---

# 🧪 Test Cases

```python
print(move_zeroes([0, 1, 0, 3, 12]))
# [1, 3, 12, 0, 0]

print(move_zeroes([0, 0, 1]))
# [1, 0, 0]

print(move_zeroes([1, 2, 3]))
# [1, 2, 3]

print(move_zeroes([0, 0, 0]))
# [0, 0, 0]

print(move_zeroes([1, 0, 2, 0, 3]))
# [1, 2, 3, 0, 0]

print(move_zeroes([]))
# []

print(move_zeroes([5]))
# [5]

print(move_zeroes([0]))
# [0]
```

---

# 1️⃣ Solution 1 — Additional List

The first solution uses a new list to collect all non-zero values.

```python
def move_zeroes(numbers):
    new_numbers = []
    zero_count = 0

    for num in numbers:
        if num != 0:
            new_numbers.append(num)
        else:
            zero_count += 1

    while zero_count > 0:
        new_numbers.append(0)
        zero_count -= 1

    return new_numbers
```

## 🔎 How It Works

The input is traversed once.

If the current number is not zero, it is added to `new_numbers`:

```python
new_numbers.append(num)
```

If the number is zero, instead of immediately adding it, the algorithm increases a counter:

```python
zero_count += 1
```

After processing all numbers, the required number of zeroes is appended to the end of the new list.

For example:

```text
Input:
[0, 1, 0, 3, 12]

Non-zero values:
[1, 3, 12]

Number of zeroes:
2

Final result:
[1, 3, 12, 0, 0]
```

---

# ⚡ Complexity — Solution 1

### Time Complexity

**O(n)**

The input is traversed once, and the zeroes are added afterward.

The total amount of work remains linear.

### Space Complexity

**O(n)**

A new list is created and can contain up to `n` elements.

Therefore:

```text
Time:  O(n)
Space: O(n)
```

---

# 2️⃣ Solution 2 — In-Place

The second solution eliminates the additional list.

```python
def move_zeroes(numbers):
    left = 0

    for num in numbers:
        if num != 0:
            numbers[left] = num
            left += 1

    while left < len(numbers):
        numbers[left] = 0
        left += 1

    return numbers
```

---

# 🔎 How It Works

The key variable is:

```python
left = 0
```

`left` represents the position where the next non-zero value should be placed.

For every non-zero number:

```python
numbers[left] = num
```

The number is written into the next available position.

Then:

```python
left += 1
```

moves the position forward.

For example:

```text
Input:
[0, 1, 0, 3, 12]
```

The non-zero values are moved toward the beginning:

```text
[1, 3, 12, ?, ?]
```

After all non-zero values have been placed, `left` points to the first position that should contain a zero.

The second loop fills the remaining positions:

```python
while left < len(numbers):
    numbers[left] = 0
    left += 1
```

Result:

```text
[1, 3, 12, 0, 0]
```

---

# 🧠 Why Does This Work?

The important observation is that the order of the non-zero elements must remain unchanged.

Therefore, we can simply place every non-zero value into the next available position from left to right.

For example:

```text
Input:
[4, 0, 7, 0, 2]

Non-zero values:
4 → 7 → 2
```

The algorithm writes them into:

```text
[4, 7, 2, ?, ?]
```

and then fills the remaining positions with zeroes:

```text
[4, 7, 2, 0, 0]
```

No additional list is required.

---

# ⚡ Complexity — Solution 2

### Time Complexity

**O(n)**

The input is traversed a constant number of times.

Even though there are two loops, the total work is still linear.

### Space Complexity

**O(1)**

Only a few variables are used:

```python
left
num
```

No additional data structure proportional to the input size is created.

Therefore:

```text
Time:  O(n)
Space: O(1)
```

---

# 📊 Comparison

| Solution   | Approach        | Time   | Extra Space |
| ---------- | --------------- | ------ | ----------- |
| Solution 1 | Additional list | `O(n)` | `O(n)`      |
| Solution 2 | In-place        | `O(n)` | `O(1)`      |

The second solution is preferable when the problem requires or benefits from in-place modification.

---

# 🔥 Optimization

The first solution was already optimal in terms of time complexity:

```text
O(n)
```

It was not possible to improve the asymptotic time complexity below `O(n)` because every element needs to be considered.

However, the memory usage could be improved.

The first solution used:

```python
new_numbers = []
```

which required `O(n)` additional space.

The optimized solution modifies the original list directly and only uses a pointer:

```python
left = 0
```

This reduces the additional space complexity from:

```text
O(n)
```

to:

```text
O(1)
```

---

# 🧠 Key Lesson

This challenge demonstrated that optimization is not always about making the algorithm faster.

Sometimes the time complexity is already optimal, but the memory usage can still be improved.

In this case:

```text
O(n) time
```

was already optimal.

The meaningful optimization was:

```text
O(n) space → O(1) space
```

The challenge also introduced an important in-place modification technique.

---

# 🔗 Connection to Previous Days

This challenge builds on concepts from previous problems.

### Day 5 — Valid Palindrome

I previously used pointer variables to control positions inside a sequence.

### Day 9 — Longest Consecutive Sequence

I learned to think about algorithmic efficiency and how the choice of data structure affects complexity.

### Day 11 — Move Zeroes

I combined these ideas by using a pointer to modify a list in place.

The important lesson is that the techniques learned on previous days can often be reused in completely different problems.

---

# 💡 What I Learned

* How to move elements while preserving their relative order.
* How to use an additional list as a simple first solution.
* How to modify a list in place.
* How to use a pointer to track the next available position.
* Why two loops can still result in `O(n)` time complexity.
* The difference between time and space optimization.
* How to reduce extra space from `O(n)` to `O(1)`.
* When further optimization is unnecessary.

---

# 🧠 Reflection

My first solution was straightforward and easy to understand.

It used an additional list to store the non-zero values and then appended the required number of zeroes.

The algorithm already had `O(n)` time complexity, but it required `O(n)` additional space.

I then created an in-place solution using a `left` pointer.

The pointer tracks where the next non-zero value should be placed. After all non-zero values have been moved, the remaining positions are filled with zeroes.

This resulted in:

```text
Time:  O(n)
Space: O(1)
```

The biggest lesson from this challenge was that an algorithm can already be optimal in time while still having room for meaningful memory optimization.

---

## ⏱️ Time Spent

Approximately: XX minutes

## 📊 Progress

**11 / 365 days completed**

**Week 2 — Day 11 🟢**

---

# 🏆 Day 11 Complete

Successfully implemented two solutions:

```text
Solution 1 → O(n) time / O(n) space
Solution 2 → O(n) time / O(1) space
```

The optimized solution modifies the input list in place while preserving the relative order of all non-zero elements.

**Day 11 / 365 🟢**
