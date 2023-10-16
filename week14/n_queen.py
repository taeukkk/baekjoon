answer = 0

def searching(queens,n):
    global answer
    row = queens[-1][0]+1
    if row==n:
        answer+=1
    possible = [1]*n
    for q in queens:
        possible[q[1]]=0
        diagonal_dec = row+q[1]-q[0]
        diagonal_inc = -row+q[0]+q[1]    
        if diagonal_inc>=0:
            possible[diagonal_inc]=0
        if diagonal_dec<n:
            possible[diagonal_dec]=0
    for i in range(n):
        if possible[i]==1:
            searching(queens+[[row,i]],n)

def solution(n):
    global answer
    for i in range(n):
        searching([[0,i]],n)
    return answer
