def analyze_numbers(numbers):
    nums_sum = sum(numbers)
    avg = nums_sum / len(numbers)
    even = len([n for n in numbers if n % 2 == 0])
    frequency = {}
    for num in numbers:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    return {
        "max": max(numbers),
        "min": min(numbers),
        "sum": nums_sum,
        "average": avg,
        "even_count": even,
        "frequency": frequency
    }


print(analyze_numbers(
    numbers = [4, 7, 2, 7, 9, 2, 4, 7]))
