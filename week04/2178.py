from collections import deque

def connection(point):
    con = []
    row, col = point[0], point[1]
    up, down, left, right = row-1, row+1, col-1, col+1

    if up>=0:
        con.append([up,col])
    if down<n:
        con.append([down,col])
    if left>=0:
        con.append([row,left])
    if right<m:
        con.append([row,right])
    
    return con

def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    while queue:
        l = queue.popleft()
        temp = connection(l)
        for t in temp:
            if not visited[t[0]][t[1]] and maze[t[0]][t[1]]!=0:
                maze[t[0]][t[1]] = maze[l[0]][l[1]]+1
                queue.append(t)
                visited[t[0]][t[1]] = 1

n,m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
bfs([0,0])
print(maze[n-1][m-1])