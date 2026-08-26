def longest_consecutive(numbers):
    numbers = sorted(set(numbers))

    if not numbers:
        return 0
    
    current_length = 1
    longest_length = 1
    for i in range(len(numbers)-1):
        if numbers[i] + 1 == numbers[i + 1]:
            current_length += 1
        else:
            current_length = 1
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