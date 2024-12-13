import math
import re


def main():
    with open("13/13.txt") as fn:
        res = [i.strip() for i in fn if i.strip()]
        chunks = [res[x:x+3] for x in range(0, len(res), 3)]
        total = 0
        for chunk in chunks:
            x,y = re.sub(r'[^0-9,]', '', chunk[0]).split(",")
            x_1,y_1 = re.sub(r'[^0-9,]', '', chunk[1]).split(",")
            x_2,y_2 = re.sub(r'[^0-9,]', '', chunk[2]).split(",")
            A = {"X":int(x),"Y":int(y)}
            B = {"X":int(x_1),"Y":int(y_1)}
            coords = {"X":int(x_2), "Y":int(y_2)}
            b = calc(coords,A,B)
            if b:
                total += b
        print(total)

def calc(coords, A, B):
    curr_min = 0
    print(A)
    print(B)
    print(coords)
    
    for i in range(100):
        totalX_B = B["X"] * i
        totalY_B = B["Y"] * i
        
        j = 0
        while True:
            totalX = totalX_B + (A["X"] * j)
            totalY = totalY_B + (A["Y"] * j)
            
            if totalX > coords["X"] or totalY > coords["Y"]:
                break
            
            if totalX == coords["X"] and totalY == coords["Y"]:
                print(f"Combination found: {i} times B and {j} times A")
                price = i*1+j*3
                if curr_min == 0:
                    curr_min = price
                elif price < curr_min:
                    curr_min = price
            
            j += 1
    return curr_min

main()