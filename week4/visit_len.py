def solution(dirs):
    answer = 0
    p = [5,5]
    move = {'L':[-1,0],'R':[1,0],'U':[0,1],'D':[0,-1]}
    dy = [[0]*11 for _ in range(10)]
    dx = [[0]*10 for _ in range(11)]
    
    for d in dirs:
        temp = [p[0]+move[d][0],p[1]+move[d][1]]
        if temp[0]<0 or temp[0]>10 or temp[1]<0 or temp[1]>10:
            continue
        else:
            if temp[0] == p[0]:
                s = p[1] if p[1]<temp[1] else temp[1]
                if dy[s][p[0]] == 0:
                    answer +=1
                    dy[s][p[0]] = 1
                
            else:
                s = p[0] if p[0]<temp[0] else temp[0]
                if dx[p[1]][s] == 0:
                    answer +=1
                    dx[p[1]][s] = 1
            p = temp
            
    return answer