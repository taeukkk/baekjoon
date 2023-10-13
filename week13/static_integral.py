def solution(k, ranges):
    answer = []
    n=0
    graph = {0:k}
    area = {}
    while k!=1:
        if k%2==0:
            k=k//2
        else:
            k = 3*k+1
        n+=1
        graph[n]=k
    for i in range(len(graph)-1):
        h = abs(graph[i]-graph[i+1])
        area[i] = max(graph[i],graph[i+1])-h/2
    for r in ranges:
        start = r[0]
        end = n+r[1]
        if end<start:
            answer.append(-1)
            continue
        result = 0
        for i in range(start,end):
            result+=area[i]
        answer.append(result)
    return answer