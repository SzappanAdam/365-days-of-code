def two_sum(numbers, target):
    seen = {}

    for index in range(len(numbers)):
        complement = target - numbers[index]
        if numbers[index] not in seen:
            seen[complement] = index
        else:
            return [seen[numbers[index]], index] 

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 5, 8, 12], 20))