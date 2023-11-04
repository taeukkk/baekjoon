def solution(n):
    answer = 0
    result = [1,1]
    for i in range(2,n+1):
        result.append((result[i-1]+result[i-2])%1000000007)

    return result[n]