def get_cost(S,E):
    if S==E:
        return 1
    elif S==0 or E==0:
        return 2
    elif abs(S-E)==2:
        return 4
    else:
        return 3
def solution(steps):
    N = len(steps)-1
    if N<2:
        return 2*N
    answer = float('inf')
    dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(N)]
    dp[0][steps[0]][0] = 2
    dp[0][0][steps[0]] = 2
    for i in range(1,N):
        E = steps[i]
        for l in range(5):
            for r in range(5):
                prev = dp[i-1][l][r]
                if prev!=float('inf'):
                    cost_l = get_cost(l,E)
                    cost_r = get_cost(r,E)
                    dp[i][E][r] = min(dp[i][E][r],prev+cost_l)
                    dp[i][l][E] = min(dp[i][l][E],prev+cost_r)
                    if i==N-1:
                        answer = min(answer,dp[i][E][r])
                        answer = min(answer,dp[i][l][E])
    return answer

steps = list(map(int,input().split()))
print(solution(steps))