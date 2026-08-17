# Day 2 — Finding Duplicates

## 🎯 Objective

Practice independent problem-solving and learn to recognize when a working solution can be simplified.

## 🧠 Topics

- Dictionaries
- Lists
- Loops
- Conditional statements
- Membership testing
- Problem-solving
- Algorithmic thinking
- Code simplification

## 💻 Challenge

Create a function called `find_duplicates()` that receives a list of integers and returns the numbers that appear at least twice.

Example:

```python
find_duplicates([4, 7, 2, 7, 9, 2, 4, 7])
```

Expected result:

```python
[7, 2, 4]
```

The order of the returned values does not have to match the example.

## 🧪 Test Cases

```python
find_duplicates([1, 2, 3, 4])
# []

find_duplicates([1, 1, 2, 3, 3, 3])
# [1, 3]

find_duplicates([5, 5, 5, 5])
# [5]
```

## 🔎 First Approach

My first solution used a dictionary to count the frequency of every number and then searched for values that appeared more than once.

Although the solution worked correctly, it collected more information than the problem actually required.

## 🚀 Improved Approach

I realized that I did not need to know exactly how many times a number appeared.

I only needed to know whether I had already encountered the number.

The improved solution therefore keeps track of previously seen numbers and adds a number to the duplicates list when it is encountered again.

## 💡 What I Learned

- A working solution is not necessarily the simplest solution.
- I should first identify exactly what information the problem requires.
- Dictionaries can be used to keep track of previously encountered values.
- Membership checks can simplify problems involving duplicates.
- Solving a problem independently is more valuable than immediately looking for an optimal solution.

## 🧠 Reflection

The first solution was more complicated than necessary because I initially focused on counting occurrences.

After reviewing the problem, I realized that counting was unnecessary. I only needed to determine whether a number had already appeared.

I was able to redesign the solution independently without using a provided solution or hint.

This was a useful exercise in improving my problem-solving approach.

## ⏱️ Time Spent

Approximately: 20 minutes

## ✅ Status

Completed