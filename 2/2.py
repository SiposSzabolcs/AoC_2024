def split_string(numbers):
    """Split a string of numbers into a list of integers."""
    return list(map(int, numbers.split()))

def is_valid_sequence(numbers):
    """Check if a sequence adheres to the safety rules."""
    is_increasing = numbers[0] < numbers[1]
    
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if not (1 <= abs(diff) <= 3):  # Tolerance check
            return False
        if (is_increasing and diff <= 0) or (not is_increasing and diff >= 0):  # Monotonicity
            return False
    
    return True

def is_safe(numbers):
    """Determine if the sequence is safe or can be made safe by removing one element."""
    if is_valid_sequence(numbers):
        return True  # Already safe
    
    # Check by removing one element at each position
    for i in range(len(numbers)):
        modified = numbers[:i] + numbers[i+1:]
        if is_valid_sequence(modified):
            return True
    
    return False

def main():
    safe_count = 0
    with open("2.txt", "r") as fn:
        lines = fn.read().splitlines()
        for line in lines:
            numbers = split_string(line)
            if is_safe(numbers):
                safe_count += 1
                print(f"Safe: {line}")
            else:
                print(f"Unsafe: {line}")
    print(f"Total safe reports: {safe_count}")

main()