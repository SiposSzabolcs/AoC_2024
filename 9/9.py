def main():
    with open("9/9.txt") as fn:
        lines = fn.readline().strip()
        print(checksum(rearrange(transformInput(lines))))

def transformInput(input):
    input = list(input)
    output = []
    isEmpty = False
    curr_id = 0
    for number in input:
        if not isEmpty:
            for i in range(int(number)):
                output.append(str(curr_id))
            curr_id += 1
        else:
            for i in range(int(number)):
                output.append(".")
        isEmpty = not isEmpty
    return output

def rearrange(input):
    r = len(input) - 1
    l = 0
    while l < r:
        if input[r] != ".":
            while input[l] != "." and l < r:
                l += 1
            if l < r:
                input[l] = input[r]
                input[r] = "."
                l += 1
        r -= 1
    return input

def checksum(input):
    curr = 0
    total = 0
    for char in input:
        if char == ".":
            pass
        else:
            total += int(char) * curr
            curr += 1
    return total

main()