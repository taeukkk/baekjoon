from collections import deque
visited = []
R,C = 0,0

def bfs(maps,start,days):
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    queue = deque([start])
    visited[start[0]][start[1]]=1
    while queue:
        merry = deque.popleft(queue)
        days+=int(maps[merry[0]][merry[1]])
        for m in move:
            row = merry[0]+m[0]
            col = merry[1]+m[1]
            if row<0 or row>=R or col<0 or col>=C:
                continue
            elif visited[row][col]!=1 and maps[row][col]!="X":
                print(row,col,maps[row][col])
                visited[row][col]=1
                queue.append([row,col])
    return days

def solution(maps):
    global R,C,visited
    R = len(maps)
    C = len(maps[0])
    visited = [[0]*C for _ in range(R)] 
    answer = []
    for i in range(R):
        for j in range(C):
            if maps[i][j]!="X" and visited[i][j]==0:
                tmp = bfs(maps,[i,j],0)
                answer.append(tmp)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer