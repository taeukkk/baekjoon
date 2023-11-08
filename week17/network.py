from collections import deque
def bfs(node,visited):
    answer = 0
    for i in range(len(node)):
        if visited[i]==0:
            queue = deque([i])
            visited[i]=1
            while queue:
                q = queue.popleft()
                connect = node[q]
                for c in connect:
                    if visited[c]==0:
                        queue.append(c)
                        visited[c]=1
            answer+=1
    return answer
def solution(n, computers):
    node = [[] for _ in range(n)]
    visited = [0]*n
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j]==1 and i!=j:
                node[i].append(j)
    return bfs(node,visited)