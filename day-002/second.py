def find_duplicates(numbers):
    seen = {}
    duplicates = []

    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        seen[num] = 1

    return duplicates

print(find_duplicates([4, 7, 2, 7, 9, 2, 4, 7]))
print(find_duplicates([1, 2, 3, 4]))
print(find_duplicates([1, 1, 2, 3, 3, 3]))
print(find_duplicates([5, 5, 5, 5]))
