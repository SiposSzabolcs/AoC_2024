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
    coords["X"] += 10000000000000
    coords["Y"] += 10000000000000
    
    ca = (coords["X"]*B["Y"] - coords["Y"] * B["X"]) / (A["X"]*B["Y"] - A["Y"]*B["X"])
    cb = (coords["X"] - A["X"] * ca) / B["X"]
    
    if ca % 1 == cb % 1 == 0:
        return ca*3+cb
    return 0

main()