def get_min(distance,visited):
    min_val = distance[0]
    index = 0
    for i in range(1,len(distance)):
        if visited[i]==1:
            continue
        if distance[i]<min_val:
            index = i
            min_val = distance[i]
    return index
        
def solution(N, road, K):
    answer = 0
    distance = [int(1e9)]*(N+1)
    visited = [0]*(N+1)
    graph = [[] for i in range(N+1)]
    for cxn in road:
        graph[cxn[0]].append([cxn[1],cxn[2]])
        graph[cxn[1]].append([cxn[0],cxn[2]])

    distance[1]=0
    visited[1]=1
    for init in graph[1]:
        distance[init[0]] = min(distance[init[0]],init[1])
    for _ in range(N-1):
        start = get_min(distance,visited)
        visited[start] = 1
        for v in graph[start]:
            cost = distance[start] +v[1] 
            if cost<distance[v[0]]:
                distance[v[0]] = cost
                
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1

    return answer