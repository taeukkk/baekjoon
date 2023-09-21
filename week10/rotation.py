from collections import deque
table = []
def rotate(query):
    global table
    x1,y1,x2,y2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
    min_value = table[x1][y1]
    value = deque([min_value])
    index = deque()
    for c in range(y1+1,y2+1):
        value.append(table[x1][c])
        index.append([x1,c])
    for r in range(x1+1,x2+1):
        value.append(table[r][y2])
        index.append([r,y2])
    for c in range(y2-1,y1-1,-1):
        value.append(table[x2][c])
        index.append([x2,c])
    for r in range(x2-1,x1-1,-1):
        value.append(table[r][y1])
        index.append([r,y1])
    min_value = min(value)
    while index:
        i = index.popleft()
        table[i[0]][i[1]] = value.popleft()
    return min_value

def solution(rows, columns, queries):
    global table
    answer = []
    for i in range(1,rows+1):
        row = []
        for j in range(1,columns+1):
            row.append((i-1)*columns+j)
        table.append(row)
    for query in queries:
        answer.append(rotate(query))
    return answer