r,c = map(int,input().split())
maze,fire,me = [],[],[]
visited = [[0]*c for _ in range(r)]

for i in range(r):
    line = list(input())
    maze.append(line)
    for j in range(c):
        if line[j] == 'F':
            fire.append([i,j])
        elif line[j] == 'J':
            me = [i,j]

def spread(index):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    for d in range(4):
        row = index[0]+dr[d]
        col = index[1]+dc[d]
        if row<0 or row>=r or col<0 or col>=c:
            continue
        elif maze[row][col]=='.' or maze[row][col]=='J':
            maze[row][col] = 'F'
            fire.append([row,col])

def bfs(start):
    queue = [[start,0]]
    visited[start[0]][start[1]] = 1
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        lq = len(queue)
        for _ in range(lq):
            q = queue.pop(0)
            if maze[q[0][0]][q[0][1]] == 'F':
                continue
            for d in range(4):
                row = q[0][0]+dr[d]
                col = q[0][1]+dc[d]
                if row <0 or row>=r or col <0 or col>=c:
                    return q[1]+1
                elif maze[row][col] == '.' and visited[row][col]==0:
                    queue.append([[row,col],q[1]+1])
                    visited[row][col] = 1
        lf = len(fire)
        for _ in range(lf):
            spread(fire.pop(0))
    return "IMPOSSIBLE"

print(bfs(me))