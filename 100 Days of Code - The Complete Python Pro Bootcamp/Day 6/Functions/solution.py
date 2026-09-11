def min_max(numbers):
    return min(numbers), max(numbers), sum(numbers)  # Returns a tuple: (min, max)

lowest, highest, total = min_max([4, 1, 9, 2]) # Unpacked directly

print(lowest, highest, total)