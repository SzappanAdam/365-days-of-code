# Day 10 — Valid Parentheses

## 🎯 Objective

Create a function that determines whether a string containing parentheses is valid.

The challenge introduces the **stack** data structure and the **LIFO (Last In, First Out)** principle.

The main goal was to recognize that when a closing bracket appears, it must match the **most recently opened** bracket.

## 🧠 Topics

* Strings
* Lists
* Dictionaries
* Stack
* LIFO (Last In, First Out)
* `append()`
* `pop()`
* Dictionary lookup
* Early returns
* Time complexity
* Space complexity

---

# 💻 Challenge

Create a function called `is_valid_parentheses()` that determines whether a string containing parentheses is valid.

The three types of brackets are:

```text
()
[]
{}
```

A string is valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket matches the most recently opened bracket.

---

# 🧪 Test Cases

```python
is_valid_parentheses("")
# True

is_valid_parentheses("()")
# True

is_valid_parentheses("()[]{}")
# True

is_valid_parentheses("(]")
# False

is_valid_parentheses("([{}])")
# True

is_valid_parentheses("([)]")
# False

is_valid_parentheses("{[]}")
# True

is_valid_parentheses("(")
# False

is_valid_parentheses(")")
# False

is_valid_parentheses("((()))")
# True

is_valid_parentheses("((()")
# False

is_valid_parentheses("{[()()]}")
# True
```

---

# 💻 Solution

```python
def is_valid_parentheses(text):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            if not stack:
                return False

            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False

    return not stack
```

---

# 🔎 How It Works

The algorithm uses a list as a **stack**.

```python
stack = []
```

Whenever an opening bracket is encountered, it is added to the stack:

```python
stack.append(char)
```

For example:

```text
(
([
([{ 
```

The most recently opened bracket is always at the end of the list.

Therefore:

```python
stack[-1]
```

returns the most recently added opening bracket.

---

# 🥞 Stack and LIFO

A stack follows the principle:

> **Last In, First Out**

This can be compared to a stack of plates.

If we put three plates on top of each other:

```text
    [3] ← last added
    [2]
    [1] ← first added
```

The first plate we can remove is `[3]`.

The same idea applies to nested parentheses:

```text
{ [ ( ) ] }
      ↑
```

The `(` was the most recently opened bracket, so it must be closed first.

This makes a stack a natural data structure for this problem.

---

# 🔄 Closing Brackets

When a closing bracket is encountered, the algorithm first checks whether the stack is empty:

```python
if not stack:
    return False
```

If the stack is empty, there is no opening bracket available to match the closing bracket.

Otherwise, the algorithm checks the most recently opened bracket:

```python
stack[-1]
```

The `pairs` dictionary tells us which opening bracket belongs to the current closing bracket:

```python
pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}
```

For example:

```python
pairs[")"]
```

returns:

```text
(
```

If the brackets match, the opening bracket is removed:

```python
stack.pop()
```

---

# 🧠 Example Walkthrough

Consider:

```text
([{}])
```

The algorithm processes the characters one by one.

### `(`

```text
stack = [
    (
]
```

### `[`

```text
stack = [
    (,
    [
]
```

### `{`

```text
stack = [
    (,
    [,
    {
]
```

### `}`

The top of the stack is `{`.

It matches `}`, so it is removed.

```text
stack = [
    (,
    [
]
```

### `]`

The top is `[`, which matches `]`.

```text
stack = [
    (
]
```

### `)`

The top is `(`, which matches `)`.

```text
stack = []
```

At the end, the stack is empty:

```python
not stack
```

therefore the function returns:

```text
True
```

---

# ❌ Invalid Example

Consider:

```text
([)]
```

After processing `(` and `[`:

```text
stack = [(, []
```

The next character is `)`.

The top of the stack is:

```text
[
```

but `)` requires:

```text
(
```

The brackets do not match, so the function immediately returns:

```text
False
```

---

# ⚡ Complexity

### Time Complexity

**O(n)**

Each character is processed once.

Stack operations such as `append()` and `pop()` are `O(1)`.

### Space Complexity

**O(n)**

In the worst case, the input may contain only opening brackets:

```text
(((((((
```

All of them must be stored in the stack.

---

# 💡 Key Lesson

The most important lesson from this challenge was understanding when a **stack** is the appropriate data structure.

The problem requires us to remember the most recently opened bracket and process it before earlier brackets.

That is exactly the behavior provided by LIFO:

```text
Last In → First Out
```

The stack therefore maps naturally onto nested structures.

---

# 🔗 Connection to Previous Days

Previous challenges focused heavily on dictionaries and sets.

This challenge introduced a different kind of data structure.

### Previous pattern

```text
Set / Dictionary
        ↓
Fast lookup
```

### New pattern

```text
Stack
        ↓
Last In, First Out
```

The important lesson is that different problems require different data structures.

The goal is not to always use the data structure I already know, but to recognize which structure naturally matches the problem.

---

# 🧠 Reflection

This was my first dedicated stack problem.

The key realization was that a closing bracket must always match the most recently opened bracket.

Using a list as a stack made this behavior straightforward:

```python
stack.append()
stack[-1]
stack.pop()
```

The final solution runs in `O(n)` time and uses `O(n)` additional space.

The challenge also reinforced the importance of selecting a data structure based on the operations the problem requires.

---

## ⏱️ Time Spent

Approximately: 30 minutes

## 📊 Progress

**10 / 365 days completed**

**Week 2 — Day 10 🟢**

---

# 🏆 Day 10 Complete

Successfully implemented a stack-based solution for validating parentheses.

```text
Time:  O(n)
Space: O(n)
```

**Day 10 / 365 🟢**