from collections import deque
t = int(input())
result = []

def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        cab = queue.popleft()
        for l in range(4):
            row = cab[0] + dr[l]
            col = cab[1] + dc[l]
            if [row,col] in cabbage and visited[row][col] == 0:
                queue.append([row,col])
                cabbage.remove([row,col])
                visited[row][col]=1
    return 1

for i in range(t):
    m,n,k = map(int, input().split())
    visited = [[0 for col in range(m)] for row in range(n)] 
    cabbage = []
    for j in range(k):
        c,r = map(int, input().split())    
        cabbage.append([r,c])

    temp = 0
    while cabbage:
        temp += bfs(cabbage.pop())
    result.append(temp)

for res in result:
    print(res)
