from collections import deque
n = int(input())
area = []
hei = set()
for _ in range(n):
    row = list(map(int, input().split()))
    area.append(row)
    temp = set(row)
    hei |= temp

def bfs(start,cnt,water):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        v = queue.popleft()
        for i in range(4):
            row = v[0] + dr[i]
            col = v[1] + dc[i]
            if row<0 or row>=n or col<0 or col>=n:
                continue
            elif visited[row][col] == 0 and area[row][col]-water>0:
                queue.append([row,col])
                visited[row][col] = 1
    return 1

result = 1
for h in hei:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = 0
    for r in range(n):
        for c in range(n):
            if area[r][c]-h>0 and visited[r][c]==0:
                temp += bfs([r,c],0,h)
    if temp > result:
        result = temp

print(result)