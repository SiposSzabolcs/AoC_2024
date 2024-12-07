from itertools import product

def main():
    with open("7/7.txt") as fn:
        cal_sum = 0
        lines = fn.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            result = splitLine(line)
            if result:
                cal_sum += result 
        print(cal_sum)
def generate_combinations(num_count):
    return product(['+', '*'], repeat=num_count - 1)

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def splitLine(line):
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))

    operator_combinations = generate_combinations(len(numbers))

    for operators in operator_combinations:
        result = evaluate_expression(numbers, operators)
        if result == target:
            return target
    
    return False

main()