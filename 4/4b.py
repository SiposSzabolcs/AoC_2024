
def main():
    count = 0
    with open("4/4.txt", "r") as fn:
        grid = fn.read().splitlines()
        for r in range(len(grid)-1):
            for c in range(len(grid[0])-1):
                if grid[r][c] != "A":continue
                corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
                if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                    count += 1
        print(count)
        
main()