def solution(n):
    answer = 0
    if n%2!=0:
        return 0
    else:
        N = n//2
        cnt = [0]*(N+1)
        cnt[1] = 3
        for i in range(2,N+1):
            cnt[i] = 3*cnt[i-1] +2
            for j in range(0,i-1):
                cnt[i] += 2*cnt[j]
        answer = cnt[N]
    return answer%1000000007