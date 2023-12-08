from collections import deque

def get_cost(prev_di,di):
    if prev_di == di:
        return 100
    else:
        return 600

def get_idx(prev_di):
    if prev_di == [1,0]:
        return 0
    elif prev_di == [0,1]:
        return 1
    elif prev_di == [-1,0]:
        return 2
    else:
        return 3

def solution(board):
    answer = float('inf')
    N = len(board)
    cost = [[[0]*4 for _ in range(N)] for _ in range(N)] 
    queue = deque([])
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    for i in range(2):
        if board[dr[i]][dc[i]]==0:
            cost[dr[i]][dc[i]][i] = 100
            queue.append([dr[i],dc[i],[dr[i],dc[i]]])
    while queue:
        q = queue.popleft()
        for i in range(4):
            row = q[0]+dr[i]
            col = q[1]+dc[i]
            if row<0 or row>=N or col<0 or col>=N:
                continue
            if board[row][col]==0 :
                prev_di = q[2]
                now_di = [dr[i],dc[i]]
                new_cost = cost[q[0]][q[1]][get_idx(prev_di)] + get_cost(prev_di,now_di)
                if cost[row][col][i]==0:
                    cost[row][col][i] = new_cost
                else:
                    if new_cost < cost[row][col][i]:
                        cost[row][col][i] = new_cost
                    else:
                        continue
                queue.append([row,col,now_di])
    for candi in cost[N-1][N-1]:
        if candi!=0:
            answer = min(answer,candi)
    return answer