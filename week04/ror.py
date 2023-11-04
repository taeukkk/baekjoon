from collections import deque

def bfs(start,maps,visited):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        q = queue.popleft()
        for i in range(4):
            row = q[0]+dr[i]
            col = q[1]+dc[i]
            if row<0 or row>=len(maps) or col<0 or col >=len(maps[0]):
                continue
            if visited[row][col]!=1 and maps[row][col]!=0:
                queue.append([row,col])
                visited[row][col] = 1
                maps[row][col] = maps[q[0]][q[1]]+1

def solution(maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    bfs([0,0],maps,visited)
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]