# Day 8 — Best Time to Buy and Sell Stock

## 🎯 Objective

Create a function that determines the maximum profit that can be achieved from a list of stock prices.

The rules are:

* Buy once.
* Sell once.
* The stock must be bought before it is sold.
* Return the maximum possible profit.
* If no profit can be made, return `0`.

The main goal was to practice single-pass algorithms and learn how to solve a problem without checking every possible buy/sell combination.

## 🧠 Topics

* Lists
* Loops
* Variables for tracking state
* Greedy-style thinking
* Single-pass algorithms
* Early returns
* Time complexity
* Space complexity
* Algorithmic optimization

---

# 💻 Challenge

Create a function called `max_profit()` that receives a list of stock prices.

The function should return the maximum possible profit from one transaction.

### Examples

```python
max_profit([7, 1, 5, 3, 6, 4])
# 5
```

The best transaction is:

```text
Buy:  1
Sell: 6
Profit: 5
```

Another example:

```python
max_profit([7, 6, 4, 3, 1])
# 0
```

No profitable transaction is possible because the price continuously decreases.

---

# 🧪 Test Cases

```python
max_profit([7, 1, 5, 3, 6, 4])
# 5

max_profit([7, 6, 4, 3, 1])
# 0

max_profit([1, 2, 3, 4, 5])
# 4

max_profit([2, 4, 1])
# 2

max_profit([3, 3, 3, 3])
# 0

max_profit([5])
# 0

max_profit([])
# 0
```

---

# 🧩 Solution

```python
def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices:
        if price - min_price > best_profit:
            best_profit = price - min_price

        if price < min_price:
            min_price = price

    return best_profit
```

---

# 🔎 How It Works

The algorithm keeps track of two important values:

```python
min_price
best_profit
```

### `min_price`

`min_price` stores the lowest stock price encountered so far.

Whenever a lower price is found, it becomes the new minimum:

```python
if price < min_price:
    min_price = price
```

This represents the best possible buying price seen up to the current point.

### `best_profit`

For every price, the algorithm calculates the profit that would be achieved by buying at the lowest price seen so far and selling at the current price:

```python
price - min_price
```

If this profit is better than the current best profit, it is stored:

```python
if price - min_price > best_profit:
    best_profit = price - min_price
```

At the end, `best_profit` contains the maximum possible profit.

---

# 🧠 Example Walkthrough

Consider:

```python
prices = [7, 1, 5, 3, 6, 4]
```

The algorithm processes the prices from left to right.

| Price | Minimum Price | Current Profit | Best Profit |
| ----: | ------------: | -------------: | ----------: |
|     7 |             7 |              0 |           0 |
|     1 |             1 |              0 |           0 |
|     5 |             1 |              4 |           4 |
|     3 |             1 |              2 |           4 |
|     6 |             1 |              5 |           5 |
|     4 |             1 |              3 |           5 |

The final result is:

```text
5
```

The important part is that when `6` is processed, the algorithm already knows that `1` was the cheapest buying price encountered before it.

---

# ⚡ Why Don't We Check Every Pair?

A straightforward approach could compare every possible buying price with every possible selling price.

For example:

```text
Buy at 7 → compare with later prices
Buy at 1 → compare with later prices
Buy at 5 → compare with later prices
...
```

This would require nested loops and result in:

```text
O(n²)
```

time complexity.

Instead, the implemented solution only needs to scan the list once.

While scanning, it remembers the cheapest price seen so far and the best profit found so far.

This allows the problem to be solved in:

```text
O(n)
```

time.

---

# 📊 Complexity

### Time Complexity

**O(n)**

The list is traversed once.

### Space Complexity

**O(1)**

Only a fixed number of variables are used regardless of the input size.

---

# 💡 Key Lesson

The most important lesson from this challenge was that not every problem requires checking every possible combination.

Instead of comparing every possible buy/sell pair, the algorithm keeps only the information that is necessary:

```text
Lowest price seen so far
+
Best profit seen so far
```

This allows the entire problem to be solved with a single pass through the input.

---

# 🧠 Reflection

This challenge was a useful step forward from the previous problems.

The solution did not require a dictionary, set, or another complex data structure.

Instead, the key was recognizing what information needed to be remembered while iterating through the list.

For every price, I:

1. Calculate the possible profit using the lowest price seen so far.
2. Update the best profit if necessary.
3. Check whether the current price is a new minimum.

The final solution runs in `O(n)` time and uses `O(1)` additional space.

One of the most important things I learned was that a solution should not always be optimized further just for the sake of optimization. If the algorithm already has an appropriate optimal complexity, additional changes may only make the code more complicated without providing a meaningful improvement.

---

## ⏱️ Time Spent

Approximately: XX minutes

## 📊 Progress

**8 / 365 days completed**

**Week 2 — Day 8 🟢**

---

# 🏆 Day 8 Complete

The challenge was solved using a single-pass algorithm with constant extra space.

**O(n) Time — O(1) Space**

**Day 8 / 365 🟢**
