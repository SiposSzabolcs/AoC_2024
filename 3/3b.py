import re

def main():
    total = 0
    with open("3/3.txt", "r") as fn:
        lines = fn.read().strip()
        mode = True
        x = re.findall("(?:don't\(\)|do\(\)|mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\))", lines)
        for line in x:
            if (line == "do()"):
                mode = True
            elif(line == "don't()"):
                mode = False
                
            if (mode == True and line != "do()" and line != "don't()"):                
                total += multiply(line)
    print(total)

def multiply(line):
    x = ''.join(filter(lambda c: c.isdigit() or c == ',', line))
    nums = x.split(",")
    return int(nums[0])*int(nums[1])
main()