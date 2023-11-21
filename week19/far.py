from collections import deque,Counter
def bfs(graph,n):
    visited = [0]*(n+1)
    distance = [0]*(n+1)
    queue = deque([1])
    visited[1] = 1
    while queue:
        node = queue.popleft()
        next_node = graph[node]
        for nn in next_node:
            if visited[nn]==0:
                visited[nn]=1
                distance[nn] = distance[node]+1
                queue.append(nn)
    return distance
    
def solution(n, edge):
    distance = [0]*(n+1)
    visited = [0]*(n+1)
    graph = {i:[] for i in range(1,n+1)}
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited[1]=1
    result = sorted(bfs(graph,n))
    max_val = result[-1]
    table = Counter(result)
    return table[max_val]