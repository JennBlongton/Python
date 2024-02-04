def generate_fibonacci_series(limit):
    fibonacci_series = [0, 1]
    while (next_num := fibonacci_series[-1] + fibonacci_series[-2]) <= limit:
        fibonacci_series.append(next_num)
    return set(fibonacci_series)

def reverse_words(input_string):
    words = input_string.split()
    fibonacci_set = generate_fibonacci_series(len(words))

    reversed_words = [word[::-1] if i not in fibonacci_set else word for i, word in enumerate(words)]
    
    return ' '.join(reversed_words)

# Example usage
input_str = "zero one one two three four five six seven eight nine ten"
output_str = reverse_words(input_str)
print(output_str)