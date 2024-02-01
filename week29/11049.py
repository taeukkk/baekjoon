def solution(N,matrix):
    if N==1:
        return matrix[0][0]*matrix[0][1]
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        dp[0][i] = matrix[i][0]
    dp[0][-1] = matrix[-1][1]
    for i in range(1,3):
        for j in range(N+1-i):
            dp[i][j] = dp[i-1][j]*dp[0][j+i]
    for i in range(3,N+1):
        for j in range(N+1-i):
            result = float('inf')
            for k in range(1,i):
                cost = 0
                if k==1:
                    cost += dp[i-1][j+1]
                elif k==i-1:
                    cost += dp[k][j]
                else:
                    cost += dp[k][j] + dp[i-k][j+k]
                cost += dp[0][j]*dp[0][j+k]*dp[0][j+i]
                result = min(result,cost)
            dp[i][j] = result
    return dp[-1][0]

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
print(solution(N,matrix))