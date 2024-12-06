def main():
    with open("6/6.txt") as fn:
        grid = [list(line) for line in fn.read().splitlines()]
        observed = ""
        rotation = "UP"
        
        
        for line in grid:
            print("".join(line))
        

        x, y = findLocation(grid)
        print("Starting position:", x, y)
        while True: 
            match rotation:
                case "UP":
                    x -= 1
                    
                    if x < 0:
                        break
                    
                    if grid[x][y] == "." or grid[x][y] == "X": 
                        print("Moving UP")
                        grid[x][y] = "^"
                        grid[x + 1][y] = "X"
                    else:
                        print("ROTATEING 90 DEGREES")
                        x += 1
                        grid[x][y] = "X"
                        rotation = "RIGHT"
                case "DOWN": 
                    x += 1
                    
                    if x > len(grid):
                        break
                    
                    if grid[x][y] == "." or grid[x][y] == "X": 
                        print("Moving DOWN")
                        grid[x][y] = "v"
                        grid[x - 1][y] = "X"
                    else:
                        print("ROTATEING 90 DEGREES")
                        x -= 1
                        grid[x][y] = "X"
                        rotation = "LEFT"
                case "RIGHT":
                    y += 1
                    
                    if y >= len(grid[0]):
                        break
                    
                    if grid[x][y] == "." or grid[x][y] == "X":
                        print("Moving RIGHT")
                        grid[x][y] = ">"
                        grid[x][y - 1] = "X"
                    else:
                        print("ROTATEING 90 DEGREES")
                        y -= 1
                        grid[x][y] = "X"
                        rotation = "DOWN"
                case "LEFT":
                    y -= 1
                    
                    if y <= 0:
                        break
                    
                    if grid[x][y] == "." or grid[x][y] == "X":
                        print("Moving LEFT")
                        grid[x][y] = "<"
                        grid[x][y + 1] = "X"
                    else:
                        print("ROTATEING 90 DEGREES")
                        y += 1
                        grid[x][y] = "X"
                        rotation = "UP"
        
        for line in grid:
            print("".join(line))
        print(countX(grid))
            
        

def findLocation(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^": 
                return i, j

def countX(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                count += 1
    return count
                

main()
