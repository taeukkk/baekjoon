from collections import deque
def bfs(graph,fee,start):
    queue = deque([])
    for node in graph[start]:
        queue.append((node,fee[start][node]))
    while queue:
        q = queue.popleft()
        neighbor = graph[q[0]]
        for nei in neighbor:
            if nei==start:
                continue
            pay = q[1]+fee[q[0]][nei]
            if fee[start][nei]==0 or fee[start][nei]>pay:
                fee[start][nei] = pay
                queue.append((nei,pay))

def solution(n, s, a, b, fares):
    N = n+1
    fee = [[0]*N for _ in range(N)]
    graph = {i:[] for i in range(1,N)}
    for f in fares:
        fee[f[0]][f[1]] = f[2]
        fee[f[1]][f[0]] = f[2]
        graph[f[0]].append(f[1])
        graph[f[1]].append(f[0])
    for i in range(1,N):
        bfs(graph,fee,i)
    answer = fee[s][a] + fee[s][b]
    for i in range(1,N):
        taxi = fee[s][i]
        muzi = fee[i][a]
        apeach = fee[i][b]
        if taxi*muzi*apeach!=0 or (taxi*muzi!=0 and i==b) or (taxi*apeach!=0 and i==a):
            answer = min(answer,taxi+muzi+apeach)
    return answer