#재귀방식
def island_dfs_recursive(grid):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(x, y):
        if x<0 or x>=m or y<0 or y>=n or grid[x][y] != '1':
            return
        grid[x][y] = 0
        for i in range(4):
            dfs_recursive(x+dx[i], y+dy[i])
        return

    for x in range(m):
        for y in range(n):
            node = grid[x][y]
            if node != '1':
                continue
            cnt += 1
            dfs_recursive(x,y)
    return cnt

