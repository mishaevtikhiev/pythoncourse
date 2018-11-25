n = int(input())
a = [[0]*n for j in range(n)]
i = 1
a[0][0] = i
dy = 0
dx = 1
x = 0
y = 0
switch = False
while True:
    if (((x+dx) // n == 0) and ((y+dy) // n == 0) and (a[y+dy][x+dx]) == 0): #note the order!
        i += 1
        y += dy
        x += dx
        a[y][x] = i
        switch = False
    elif (dx == 1) and (dy == 0):
        dx = 0
        dy = 1
        if (a[(y+dy) % n][(x+dx) % n] > 0):
            switch = True
    elif (dx == 0) and (dy == 1):
        dx = -1
        dy = 0
        if (a[(y+dy) % n][(x+dx) % n] > 0):
            switch = True
    elif (dx == -1) and (dy == 0):
        dx = 0
        dy = -1
        if (a[(y+dy) % n][(x+dx) % n] > 0):
            switch = True
    elif (dx == 0) and (dy == -1):
        dy = 0
        dx = 1
        if (a[(y+dy) % n][(x+dx) % n] > 0):
            switch = True
    if (switch):
        break
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
