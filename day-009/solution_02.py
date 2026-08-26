def longest_consecutive(numbers):
    seen = set(numbers)

    if not seen:
        return 0

    current_number = 0
    current_length = 0
    longest_length = 0
    for x in seen:
        if x - 1 not in seen:
            current_number = x
            current_length = 1 
        while current_number + 1 in seen:
            current_number += 1
            current_length += 1
        if current_length > longest_length:
            longest_length = current_length
    return longest_length

print(longest_consecutive([100, 4, 200, 1, 3, 2])) # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longest_consecutive([1, 2, 3, 4, 5])) # 5
print(longest_consecutive([5])) # 1
print(longest_consecutive([])) # 0
print(longest_consecutive([10, 5, 20, 15])) # 1
print(longest_consecutive([1, 2, 2, 3])) # 3
print(longest_consecutive([-2, -1, 0, 1, 2])) # 5