from collections import deque
def sliding(start,board,direction):
    r = start[0]
    c = start[1]
    while True:
        dr = r+direction[0]
        dc = c+direction[1]
        if dr<0 or dr>=len(board) or dc<0 or dc>=len(board[0]) or board[dr][dc]=='D':
            return [r,c]
        r=dr
        c=dc
    return [-1,-1]

def bfs(start,board):
    cnt = 10001
    visited = []
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    queue = deque([start+[0]])
    visited.append(start)
    while queue:
        q = queue.popleft()
        for m in move:
            stop = sliding(q[:2],board,m)
            if stop[0] == -1 or stop == q[:2] or stop in visited:
                continue
            if board[stop[0]][stop[1]] =='G':
                cnt = min(cnt,q[2]+1)
            queue.append(stop+[q[2]+1])
            visited.append(stop)
    return cnt

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='R':
                answer= bfs([i,j],board)
                if answer == 10001:
                    return -1
                return answer