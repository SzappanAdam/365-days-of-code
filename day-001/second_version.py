def analyze_numbers(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    nums_sum = 0
    length = 0
    even_count = 0
    frequency = {}
    
    for num in numbers:
        # Maximum
        if num > maximum:
            maximum = num

        # Minimum
        elif num < minimum:
            minimum = num

        # Sum
        nums_sum += num

        # Length for average
        length += 1

        # Count even numbers
        if num % 2 == 0:
            even_count += 1

        # Frequency 
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    # Average    
    avg = nums_sum / length

    return {
        "max": maximum,
        "min": minimum,
        "sum": nums_sum,
        "average": avg,
        "even_count": even_count,
        "frequency": frequency
    }


print(analyze_numbers(
    numbers = [4, 7, 2, 7, 9, 2, 4, 7]))