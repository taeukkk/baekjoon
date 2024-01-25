def solution(N):
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(dp)
    return sum(dp[N])%1000000000

N = int(input())
print(solution(N))