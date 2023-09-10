result = []
def triangle(start,num,n):
    r = start[0]
    c = start[1]
    i,j=0,0
    if n<1:
        return
    
    for i in range(r,r+n):
        result[i][c] = num
        num+=1
    for j in range(c+1,c+n):
        result[i][j] = num
        num+=1
    for i in range(r+n-2,r,-1):
        j-=1
        result[i][j] = num
        num+=1
    triangle([i+1,j],num,n-3)

def solution(n):
    for i in range(n):
        result.append([0]*(i+1))
    triangle([0,0],1,n)
    answer = []
    for row in result:
        for col in row:
            answer.append(col)
    return answer