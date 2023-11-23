def get_range(idx,n,w):
    result = [idx-w,idx+w]
    if result[0]<=0:
        result[0]=1
    if result[1]>n:
        result[1]=n
    return result

def put_station(blank,w):
    answer = 0
    width = 2*w+1
    cnt = blank[1]-blank[0]+1
    if cnt%width==0:
        answer+=cnt//width
    else:
        answer+=cnt//width+1
    return answer
    
def solution(n, stations, w):
    answer = 0
    start = get_range(stations[0],n,w)
    if start[0]!=1:
        answer += put_station([1,start[0]-1],w)
    end = get_range(stations[-1],n,w)
    if end[1]!=n:
        answer += put_station([end[1]+1,n],w)
    for i in range(len(stations)-1):
        range_s = get_range(stations[i],n,w)
        range_e = get_range(stations[i+1],n,w)
        answer += put_station([range_s[1]+1,range_e[0]-1],w)
    return answer