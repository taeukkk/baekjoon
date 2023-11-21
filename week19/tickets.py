N = 0
answer = []
def dfs(node, graph, flight, visited):
    if len(flight) == N:
        answer.append(flight)
        return 
    if node not in graph:
        return 
    next_node = graph[node]
    for nn in next_node:
        ticket = node+"/"+nn
        if visited[ticket]!=0:
            visited[ticket] -= 1
            dfs(nn,graph,flight+[nn],visited)
            visited[ticket] += 1 

def solution(tickets):
    global N,answer
    N = len(tickets)+1 
    graph,visited = {},{}
    for ticket in tickets:
        start,end = ticket
        key = start+"/"+end
        if key in visited:
            visited[key]+=1
        else:
            visited[key]=1
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    dfs("ICN",graph,["ICN"],visited)
    answer.sort()
    return answer[0]