from collections import deque
def add_graph(key,val,graph):
    if key in graph:
        graph[key].append(val)
    else:
        graph[key] = [val]
def get_result(val):
    if val==float('inf'):
        return -1
    else:
        return val

def solution(n, roads, sources, destination):
    answer = []
    destination -=1
    moves = {i:[] for i in range(n)}
    graph = {}
    for road in roads:
        S,E = road 
        add_graph(S-1,E-1,graph)
        add_graph(E-1,S-1,graph)
    queue = deque([destination])
    D = [float('inf')]*n
    D[destination] = 0
    visited = [0]*n
    visited[destination] = 1
    queue = deque([destination])
    while queue:
        q = queue.popleft()
        if q in graph:
            nodes = graph[q]
            for node in nodes:
                if visited[node]==0:
                    D[node] = D[q]+1
                    queue.append(node)
                    visited[node] = 1
    for source in sources:
        s = source-1
        answer.append(get_result(D[s]))
    return answer