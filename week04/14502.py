from collections import deque
from itertools import combinations

n,m = map(int,input().split())
lab,virus,space = [],[],[]
for i in range(n):
    row = list(map(int,input().split()))
    lab.append(row)
    for j in range(m):
        if row[j] == 2:
            virus.append([i,j])
        elif row[j] ==0:
            space.append([i,j])
new_walls = list(combinations(space,3))

def bfs(start,wall):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    cnt = 1
    while queue:
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        s = queue.popleft()
        for i in range(4):
            row = s[0] + dr[i]
            col = s[1] + dc[i]
            if row<0 or row>=n or col<0 or col>=m:
                continue
            elif  visited[row][col] == 0 and [row,col] not in wall and lab[row][col] !=1:
                queue.append([row,col])
                visited[row][col] = 1
                cnt+=1
    return cnt

result = n*m
for w in new_walls:
    visited = [[0]*m for _ in range(n)]
    temp = 0
    for v in virus:
        if visited[v[0]][v[1]]!=1:
            temp+=(bfs(v,w))
    if temp <result:
        result = temp

print(len(space)+len(virus)-3-result)