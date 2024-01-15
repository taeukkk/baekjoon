def solution(N,arr):
    L,R = [0]*N,[0]*N
    L[0] = arr[0]
    R[-1] = arr[-1]
    for i in range(1,N):
        L[i] = max(L[i-1]+arr[i],arr[i])
        j = N-1-i
        R[j] = max(R[j+1]+arr[j],arr[j])
    answer = max(L)
    for i in range(1,N-1):
        answer = max(answer,L[i-1]+R[i+1])
    return answer

N = int(input())
arr = list(map(int,input().split()))
print(solution(N,arr))