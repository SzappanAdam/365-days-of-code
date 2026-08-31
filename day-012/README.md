# Day 12 — Best Time to Buy and Sell Stock II

## 🎯 Objective

Create a function that calculates the maximum possible profit from buying and selling a stock multiple times.

Unlike the previous stock problem, multiple transactions are allowed.

The main goal was to recognize that every positive price increase can contribute to the total profit.

---

## 🧠 Topics

* Lists
* Loops
* Greedy algorithms
* Local vs. global optimization
* Single-pass algorithms
* Time complexity
* Space complexity
* Comparing consecutive elements

---

# 💻 Challenge

Given a list of daily stock prices, calculate the maximum possible profit.

The rules are:

* You can buy and sell multiple times.
* You can hold at most one stock at a time.
* You must buy before selling.
* You cannot hold multiple stocks simultaneously.
* The goal is to maximize total profit.

---

## 📌 Example

```python
max_profit_multiple([7, 1, 5, 3, 6, 4])
# 7
```

One possible strategy is:

```text
1 → 5 = +4
3 → 6 = +3

Total profit = 7
```

---

# 🧪 Test Cases

```python
print(max_profit_multiple([7, 1, 5, 3, 6, 4]))
# 7

print(max_profit_multiple([1, 2, 3, 4, 5]))
# 4

print(max_profit_multiple([7, 6, 4, 3, 1]))
# 0

print(max_profit_multiple([1, 5, 2, 8]))
# 10

print(max_profit_multiple([3, 3, 3, 3]))
# 0

print(max_profit_multiple([2, 4, 1, 7]))
# 8

print(max_profit_multiple([5]))
# 0

print(max_profit_multiple([]))
# 0
```

---

# 💻 Solution

```python
def max_profit_multiple(prices):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]

    return profit
```

---

# 🔎 How It Works

The algorithm compares every pair of consecutive prices.

If the next day's price is higher:

```python
prices[i] < prices[i + 1]
```

the difference is added to the total profit:

```python
profit += prices[i + 1] - prices[i]
```

If the next day's price is lower or equal, nothing is added.

---

# 🧠 The Key Insight

The important observation is that every profitable increase should be collected.

Consider:

```text
1 → 2 → 3 → 4 → 5
```

Instead of treating this as one transaction:

```text
1 → 5 = +4
```

we can calculate:

```text
1 → 2 = +1
2 → 3 = +1
3 → 4 = +1
4 → 5 = +1
```

Therefore:

```text
1 + 1 + 1 + 1 = 4
```

The total profit is identical.

This means we do not need to explicitly track individual buy and sell transactions.

We only need to collect every positive price difference.

---

# 📊 Example Walkthrough

For:

```text
[7, 1, 5, 3, 6, 4]
```

we compare neighboring values:

```text
7 → 1
```

Price decreases, so:

```text
profit = 0
```

Then:

```text
1 → 5
```

Price increases:

```text
profit = 4
```

Then:

```text
5 → 3
```

Price decreases:

```text
profit = 4
```

Then:

```text
3 → 6
```

Price increases:

```text
profit = 7
```

Finally:

```text
6 → 4
```

Price decreases, so the final result remains:

```text
profit = 7
```

---

# 🧠 Greedy Approach

This solution uses a **greedy algorithm**.

The algorithm makes a locally optimal decision at every step:

> If tomorrow's price is higher than today's price, take the profit from that increase.

There is no reason to ignore a positive increase because the stock can be sold and bought again on consecutive days.

For example:

```text
1 → 2 → 3
```

Taking:

```text
1 → 2
```

and:

```text
2 → 3
```

produces:

```text
+1 +1 = +2
```

which is exactly the same as buying at `1` and selling at `3`.

---

# ⚡ Complexity

### Time Complexity

**O(n)**

The list is traversed once.

For each element, only a constant amount of work is performed.

### Space Complexity

**O(1)**

Only the `profit` variable and the loop index are used.

No additional data structure is created.

Therefore:

```text
Time:  O(n)
Space: O(1)
```

---

# 🔗 Connection to Day 8

This challenge is directly related to the previous stock problem.

### Day 8

The goal was to find the maximum profit from **one transaction**.

The solution needed to track:

```python
min_price
best_profit
```

because we had to find the best possible buying and selling points.

### Day 12

Multiple transactions are allowed.

Because of this, we can simply collect every positive price difference.

The problem therefore becomes much simpler.

```text
Day 8:
Find the best single transaction

Day 12:
Collect every profitable increase
```

This is a good example of how a small change in the problem rules can lead to a completely different algorithm.

---

# 💡 What I Learned

* How a greedy algorithm can solve a problem with a single pass.
* How to recognize when local improvements can be safely accumulated.
* How comparing neighboring values can simplify a problem.
* Why explicit buy/sell tracking is unnecessary in this version.
* How to reason about `O(n)` time complexity.
* How to achieve `O(1)` extra space.
* How the same general problem can require a different algorithm when its constraints change.

---

# 🧠 Reflection

I initially expected this problem to require tracking buying and selling points, similar to the previous stock problem.

However, because multiple transactions are allowed, I realized that every positive difference between consecutive prices can be added to the total profit.

For example:

```text
1 → 2 → 3 → 4
```

can be viewed as:

```text
+1 +1 +1
```

which produces the same total profit as:

```text
1 → 4 = +3
```

This allowed me to create a very simple greedy solution.

The final algorithm runs in:

```text
O(n)
```

time and:

```text
O(1)
```

extra space.

I found the optimal solution on the first attempt without needing a second version.

---

## ⏱️ Time Spent

Approximately: 20 minutes

## 📊 Progress

**12 / 365 days completed**

**Week 2 — Day 12 🟢**

---

# 🏆 Day 12 Complete

Successfully implemented the maximum-profit algorithm for unlimited stock transactions.

```text
Time:  O(n)
Space: O(1)
Approach: Greedy
```

The solution collects every profitable consecutive price increase.

**Day 12 / 365 🟢**
