from collections import deque
def bfs(start,maps,visited,end):
    cnt = 10001
    queue = deque([start+[0]])
    visited[start[0]][start[1]]=1
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    while queue:
        q = queue.popleft()
        for m in move:
            row = q[0]+m[0]
            col = q[1]+m[1]
            if row<0 or row>=len(maps) or col<0 or col>=len(maps[0]):
                continue
            if end == [row,col]:
                cnt = min(q[2]+1,cnt)
            elif visited[row][col]==0 and maps[row][col]!='X':
                queue.append([row,col]+[q[2]+1])
                visited[row][col]=1
    return cnt

def solution(maps):
    answer = 0
    s,l,e = [],[],[]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                s = [i,j]
            elif maps[i][j]=='L':
                l=[i,j]
            elif maps[i][j]=='E':
                e=[i,j]
        if s and l and e:
            break
        
    step1 = bfs(s,maps,[[0]*len(maps[0]) for _ in range(len(maps))],l)
    step2 = bfs(l,maps,[[0]*len(maps[0]) for _ in range(len(maps))],e)
    if step1==10001 or step2==10001:
        return -1
    return step1+step2