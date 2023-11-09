def solution(n, s):
    base = s//n
    if base<1:
        return [-1]
    answer = [base]*n
    extra = s-base*n
    for i in range(n-1,n-1-extra,-1):
        answer[i]+=1
    return answer