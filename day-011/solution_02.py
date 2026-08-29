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

print(move_zeroes([0, 1, 0, 3, 12])) # [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1])) # [1, 0, 0]
print(move_zeroes([1, 2, 3])) # [1, 2, 3]
print(move_zeroes([0, 0, 0])) # [0, 0, 0]
print(move_zeroes([1, 0, 2, 0, 3])) # [1, 2, 3, 0, 0]
print(move_zeroes([])) # []
print(move_zeroes([5])) # [5]
print(move_zeroes([0])) # [0]