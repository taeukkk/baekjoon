def solution(board):
    answer = 0
    R,C = len(board),len(board[0])
    area = [[0]*C for _ in range(R)]
    area[0][0]=board[0][0]
    for i in range(1,R):
        if board[i][0]==1:
            area[i][0]=1
    for j in range(1,C):
        if board[0][j]==1:
            area[0][j]=1
            
    for i in range(1,R):
        for j in range(1,C):
            if board[i][j]==1:   
                area[i][j] = min(area[i-1][j-1],area[i-1][j],area[i][j-1])+1
    for row in area:
        for col in row:
            answer = max(answer,col)
    return answer**2