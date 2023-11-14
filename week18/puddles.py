def get_count(up,left):
    if up==-1 and left==-1:
        return 0
    elif up==-1 and left!=-1:
        return left
    elif up!=-1 and left==-1:
        return up
    else:
        return up+left

def solution(m, n, puddles):
    answer = 0
    shortcut = [[0]*m for _ in range(n)]
    for p in puddles:
        shortcut[p[1]-1][p[0]-1]=-1
    for i in range(1,m):
        if shortcut[0][i]==-1:
            break
        shortcut[0][i]=1
    for j in range(1,n):
        if shortcut[j][0]==-1:
            break
        shortcut[j][0]=1

    for j in range(1,n):
        for i in range(1,m):
            if shortcut[j][i]==-1:
                continue
            shortcut[j][i] += get_count(shortcut[j-1][i],shortcut[j][i-1])
    answer = shortcut[n-1][m-1]%1000000007
    return answer