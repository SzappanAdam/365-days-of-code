def find_duplicates(numbers):
    seen = {}
    duplicates = []

    for num in numbers:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    for num in seen.items():
        if num[1] > 1:
            duplicates.append(num[0])

    return duplicates


print(find_duplicates([4, 7, 2, 7, 9, 2, 4, 7]))
print(find_duplicates([1, 2, 3, 4]))
print(find_duplicates([1, 1, 2, 3, 3, 3]))
print(find_duplicates([5, 5, 5, 5]))
