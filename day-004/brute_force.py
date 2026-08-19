def two_sum_brute_force(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

print(two_sum_brute_force([2, 7, 11, 15], 9))
print(two_sum_brute_force([3, 2, 4], 6))
print(two_sum_brute_force([3, 3], 6))
print(two_sum_brute_force([1, 5, 8, 12], 20))