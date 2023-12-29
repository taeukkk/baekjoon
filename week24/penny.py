def solution(n, money):
    dp = [0]*(n+1)
    dp[0]=1
    for M in money:
        for i in range(1,n+1):
            j = i-M
            if j>=0:
                dp[i]+=dp[j]
    return dp[n]%1000000007