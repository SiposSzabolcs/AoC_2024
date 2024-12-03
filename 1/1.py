def splitLists(nums):
    left = []
    right = []
    total = 0
    for numbers in nums:
        numbs = numbers.split("  ")
        numbs = list(map(int, numbs))
        left.append(numbs[0])
        right.append(numbs[1])
        
    left.sort()
    right.sort()
    
    for i in range(len(left)):
        if (left[i] in right):
            total += left[i] * right.count(left[i])
    return total

def getDistance(num1, num2):
    distance = abs(num1 - num2)
    return distance

def main():
    
    with open("1.txt", "r") as fn:
        numbers = fn.read().splitlines()
        print(splitLists(numbers))
        
main()