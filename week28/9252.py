def solution(words):
    answer = ''
    N,M = len(words[0])+1,len(words[1])+1
    dp = [[0]*N for _ in range(M)]
    for i in range(1,M):
        for j in range(1,N):
            if words[0][j-1] == words[1][i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    i,j = M-2,N-2
    while i>=0 and j>=0:
        if words[0][j]==words[1][i]:
            answer += words[0][j]
            i-=1
            j-=1
        else:
            if dp[i+1][j]>dp[i][j+1]:
                j-=1
            else:
                i-=1
    return answer[::-1]

words = []
for _ in range(2):
    words.append(input())
answer = solution(words)
print(len(answer))
print(answer)