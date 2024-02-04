def solution(i,v):
    global N,M,dp,graph
    if v==M-1:
        if graph[i][0]!=0:
            return graph[i][0]
        return float('inf')
    if dp[i][v] != 0:
        return dp[i][v]
    for j in range(N):
        J = 1<<j
        if v&J==0 and graph[i][j]!=0:
            if dp[i][v]==0:
                dp[i][v] = solution(j,v|J)+graph[i][j]
            else:
                dp[i][v] = min(dp[i][v],solution(j,v|J)+graph[i][j])
    if dp[i][v]==0:
        return float('inf')
    return dp[i][v]

N = int(input())
M = (1<<N)
dp = [[0]*M for _ in range(N)]
graph = [list(map(int,input().split())) for _ in range(N)]
print(solution(0,1))