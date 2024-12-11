from collections import defaultdict

def solve_plutonian_pebbles_optimized(num_blinks):
    
    input = "773 79858 0 71 213357 2937 1 3998391"
    input_list = input.split(" ")
    initial_stones = [int(input) for input in input_list]


    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1

    for _ in range(num_blinks):
        new_stone_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                mid = len(s) // 2
                new_stone_counts[int(s[:mid])] += count
                new_stone_counts[int(s[mid:])] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    total_stones = sum(stone_counts.values())
    return total_stones

print(solve_plutonian_pebbles_optimized(75))