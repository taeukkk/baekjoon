def solution(m, n, board):
    table = []
    for i in range(m):
        table.append(list(board[i]))
    answer = 0
    check = [[0,0],[0,1],[1,1],[1,0]]

    while True:
        bomb = set()
        for i in range(m-1):#row
            for j in range(n-1):#col
                if table[i][j]=="-":
                    continue;
                if table[i][j]==table[i][j+1] and table[i][j]==table[i+1][j] and table[i][j]==table[i+1][j+1]:
                    for c in check:
                        bomb.add((i+c[0],j+c[1]))
        if not bomb:
            break;
        for b in bomb:
            table[b[0]][b[1]] = "-"
            answer +=1

        for j in range(n):#col
            for i in range(m-1,0,-1):#row
                if table[i][j]!="-":
                    continue;
                for k in range(i-1,-1,-1):
                    if table[k][j]=="-":
                        continue;
                    table[i][j],table[k][j] = table[k][j],table[i][j]
                    break;

    return answer