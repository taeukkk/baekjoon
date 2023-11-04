n = int(input())
queen = 0
col = [0]*n
l_to_r = [0]*(2*n-1)
r_to_l = [0]*(2*n-1)

def check_board(r,c,val):
    col[c]=val
    l_to_r[r+c]=val
    r_to_l[n-1-c+r]=val

def solution(cnt,prev):
    global queen
    if cnt == n:
        queen+=1
    row = prev+1
    for i in range(n):
        if col[i]==0 and l_to_r[row+i]==0 and r_to_l[n-1-i+row]==0:
            check_board(row,i,1)
            solution(cnt+1,row)
            check_board(row,i,0)

for i in range(n):
    check_board(0,i,1)
    solution(1,0)
    check_board(0,i,0)
    
print(queen)
