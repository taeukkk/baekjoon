import sys
import copy
from itertools import combinations
input = sys.stdin.readline
n,m = map(int,input().split())
cctv,table = [],[]
answer = n*m
for i in range(n):
    row = list(map(int,input().split()))
    table.append(row)
    for j in range(m):
        if 0< row[j] <6:
            cctv.append([i,j])
num_cctv = len(cctv)

def check(s,move,board):
    for d in move:
        r = s[0]+d[0]
        c = s[1]+d[1]
        while(r>=0 and r<n and c>=0 and c<m):
            if board[r][c]==6:
                break;
            elif board[r][c]==0:
                board[r][c] ='#'
            r += d[0]
            c += d[1]
    return board

def solution(cnt,board):
    global answer
    if cnt == num_cctv:
        blank = 0
        for row in board:
            for col in row:
                if col==0:
                    blank+=1
        if blank<answer:
            answer = blank
        return;
    
    p = cctv[cnt]
    c = table[p[0]][p[1]]
    if c==1:
        direction = [ [1,0], [-1,0], [0,1], [0,-1] ]
        for d in direction:
            checked = check(p,[d],copy.deepcopy(board))
            solution(cnt+1,checked)
    elif c==2:
        direction = [ [[1,0],[-1,0]], [[0,1],[0,-1]] ]
        for d in direction:
            checked = check(p,d,copy.deepcopy(board))
            solution(cnt+1,checked)
    elif c==3:
        direction = [ [[1,0],[0,1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[-1,0],[0,-1]] ]
        for d in direction:
            checked = check(p,d,copy.deepcopy(board))
            solution(cnt+1,checked)
    elif c==4:
        direction = list(combinations([[1,0],[-1,0],[0,1],[0,-1]],3))
        for d in direction:
            checked = check(p,d,copy.deepcopy(board))
            solution(cnt+1,checked)
    else:
        d = [[1,0],[-1,0],[0,1],[0,-1]] 
        checked = check(p,d,board)
        solution(cnt+1,checked)
    
solution(0,table)
print(answer)