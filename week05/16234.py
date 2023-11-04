n,l,r = map(int,input().split())
area = [list(map(int, input().split())) for _ in range(n)]

def bfs(start,act):
    queue = [start]
    visited[start[0]][start[1]] = 1

    num = area[start[0]][start[1]]
    cnt=1
    link = [start]

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        q = queue.pop(0)
        for d in range(4):
            row = q[0] + dr[d]
            col = q[1] + dc[d]
            if row<0 or row>=n or col<0 or col>=n:
                continue
            elif l<= abs(area[row][col]-area[q[0]][q[1]]) <=r and visited[row][col]!=1:
                queue.append([row,col])
                visited[row][col] = 1
                num += area[row][col]
                cnt+=1
                link.append([row,col])

    return [num,cnt,link]

answer = 0
while True:
    visited = [[0]*n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=1:
                result.append(bfs([i,j],[]))
    if len(result) == n*n:
        break

    for res in result:
        if len(res[2])!=1:
            for p in res[2]:
                area[p[0]][p[1]] = res[0]//res[1]
    answer +=1
print(answer)