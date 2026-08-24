def contains_duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1])) # True
print(contains_duplicate([1, 2, 3, 4])) # False
print(contains_duplicate([1, 1])) # True
print(contains_duplicate([])) # False
print(contains_duplicate([5, 5, 5, 5])) # True
print(contains_duplicate([1, 2, 3, 4, 5, 6])) # False