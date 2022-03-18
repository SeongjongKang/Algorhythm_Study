# stdin으로하면 왜 안될까
# from sys import stdin

n = int(input())
num = []
count = []
for i in range(n):
    num.append(list(map(int,input())))

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n or num[x][y] != 1:
        return False
    num[x][y] = 0
    global c
    c += 1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
c = 0
complex = 0
for x in range(n):
    for y in range(n):
        if dfs(x,y) is True:
            count.append(c)
            c = 0
            complex += 1
count.sort()
print(complex)
for i in range(len(count)):
    print(count[i])

