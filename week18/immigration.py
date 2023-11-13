import bisect
def get_sum(times,limit):
    result = 0
    idx = bisect.bisect_right(times,limit)
    for i in range(idx):
        result+=limit//times[i]
    return result
    
def solution(n,times):
    answer = 0
    times.sort()
    start,end = 0, 10**5
    while get_sum(times,end)<n:
        end*=10
    while start <= end:
        mid = (start+end)//2
        t = get_sum(times,mid)
        if t<n:
            start = mid+1
        else:
            end = mid-1
            if get_sum(times,end)<n:
                answer = mid
                break;
    return answer