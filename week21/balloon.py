def solution(a):
    answer = 2
    L = len(a)
    min_left,min_right = [10**9+1]*L,[10**9+1]*L
    min_left[0] = a[0]
    min_right[-1] = a[-1]
    for i in range(1,L):
        min_left[i] = min(min_left[i-1],a[i])
        min_right[L-1-i] = min(min_right[L-i],a[L-1-i])
    for i in range(1,L-1):
        if min_left[i-1]<a[i] and min_right[i+1]<a[i]:
            continue
        answer+=1
    return answer