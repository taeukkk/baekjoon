import copy
import sys
input = sys.stdin.readline
n = int(input())
table = [list(map(int,input().split())) for _ in range(n)]
result = 2
direction = [[1,0],[-1,0],[0,1],[0,-1]] # up,down,left,right
back = [[1,n,1,-1],[n-2,-1,-1,n]]

def get_max(board):
    global result
    for row in board:
        for col in row:
            if col>result:
                result = col

def action(d,b,board):
    for i in range(n): 
        is_merge = [0]*n
        if d[1]==0: #up and down
            for j in range(b[0],b[1],b[2]): #row
                for k in range(j,b[0]-b[2],-b[2]):
                    if board[k-d[0]][i]==0:
                        board[k-d[0]][i] += board[k][i]
                        board[k][i] = 0
                        if is_merge[k]==1:
                            is_merge[k-d[0]] = 1
                            is_merge[k]=0
                    elif board[k][i]==board[k-d[0]][i]:
                        if is_merge[k-d[0]]==0 and is_merge[k]==0:
                            board[k-d[0]][i] += board[k][i]
                            board[k][i] = 0
                            is_merge[k-d[0]] = 1
        else: #left and right
            for j in range(b[0],b[1],b[2]): #col
                for k in range(j,b[0]-b[2],-b[2]):
                    if board[i][k-d[1]]==0:
                        board[i][k-d[1]] += board[i][k]
                        board[i][k] = 0
                        if is_merge[k]==1:
                            is_merge[k-d[1]] = 1
                            is_merge[k]=0
                    elif board[i][k] == board[i][k-d[1]]:
                        if is_merge[k]==0 and is_merge[k-d[1]]==0:
                            board[i][k-d[1]] += board[i][k]
                            board[i][k] = 0
                            is_merge[k-d[1]] = 1
    return board

def solution(cnt,board):
    if cnt==5:
        return;
    for i in range(4):
        moved = action(direction[i],back[i%2],copy.deepcopy(board))
        get_max(moved)
        solution(cnt+1,moved)

solution(0,table)
print(result)