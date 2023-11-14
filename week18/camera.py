def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    car = routes[0][1]
    idx = 1
    while idx<len(routes):
        start = routes[idx][0]
        if start>car:
            answer+=1
            car = routes[idx][1]
        idx+=1
    return answer+1