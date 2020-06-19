import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()] # 10 10     Building has 100 windows (10x10)
n = int(input())  # maximum number of turns before game over. Batman has 6 jumps to find the bombs
x0, y0 = [int(i) for i in input().split()] #Batman starts at position (2,5)
lx = 0
ly = 0
hx = w-1
hy = h-1

x0 = (w-1)//2
y0 = (h-1)//2
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if h > 50:
        if len(bomb_dir) > 1:
            if bomb_dir[1] == 'L':
                hx = x0 - 1
            elif bomb_dir[1] == 'R':
                lx = x0 + 1
            if bomb_dir[0] == 'U':
                hy = y0 - 5
            else:
                ly = y0 + 5
        else:
            if bomb_dir[0] == 'L':
                hx = x0 - 1
            elif bomb_dir[0] == 'R':
                lx = x0 + 1
            elif bomb_dir[0] == 'U':
                hy = y0 - 5
            else:
                ly = y0 + 5
        x0 = (hx + lx) // 2
        y0 = (hy + ly) // 2
    if len(bomb_dir) > 1:
        if bomb_dir[1] == 'L':
            hx = x0-1
        elif bomb_dir[1] == 'R':
            lx = x0+1
        if bomb_dir[0] == 'U':
            hy = y0-1
        else:
            ly = y0+1
    else:
        if bomb_dir[0] == 'L':
            hx = x0-1
        elif bomb_dir[0] == 'R':
            lx = x0+1
        elif bomb_dir[0] == 'U':
            hy = y0-1
        else:
            ly = y0+1
    x0 = (hx+lx)//2
    y0 = (hy+ly)//2
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # the location of the next window Batman should jump to.
    print(x0,y0)
