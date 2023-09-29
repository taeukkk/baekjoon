from collections import deque
def check_distance(place,start,visited):
    queue = deque([start+[0]])
    visited[start[0]][start[1]]=1
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    while queue:
        q = queue.popleft()
        for m in move:
            row = q[0]+m[0]
            col = q[1]+m[1]
            if row<0 or row>=5 or col<0 or col>=5:
                continue
            if visited[row][col]!=1:
                if q[2]==0:
                    if place[row][col]=='P':
                        return 0
                    else:
                        queue.append([row,col,1])
                        visited[row][col]=1
                if q[2]==1 and place[row][col]=='P':
                    if place[q[0]][q[1]]!='X':
                        return 0
    return 1
def solution(places):
    answer = [1]*5
    for n in range(5):#대기실n
        visited = [[0]*5 for _ in range(5)]
        for i in range(5):#row
            for j in range(5):#col
                if places[n][i][j]=='P':
                    if check_distance(places[n],[i,j],visited)==0:
                        answer[n]=0
                        break;
            if answer[n]==0:
                break;
    return answer