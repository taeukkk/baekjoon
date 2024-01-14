def solution(N,schedule):
    dp = [0]*(N+1)
    for i in range(N-1,-1,-1):
        j = i+schedule[i][0]
        if j<=N:
            dp[i] = max(dp[i+1],dp[j]+schedule[i][1])
        else:
            dp[i]=dp[i+1]
    return dp[0]

N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]
print(solution(N,schedule))