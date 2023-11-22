from collections import deque
from copy import deepcopy

def update_ranking(table,indegree,queue):
    while queue:
        i = queue.popleft()
        next_node = deepcopy(table[i][0])
        prev_node = deepcopy(table[i][1])
        for n in next_node:
            indegree[n]-=1
            if indegree[n]==0:
                queue.append(n)
            win = table[n][0]
            lose = table[i][1]
            table[n][1] |= lose
            table[i][0] |= win
        for p in prev_node:
            win = table[i][0]
            lose = table[p][1]
            table[p][0] |= win
            table[i][1] |= lose
    return table

def solution(n, results):
    answer = 0
    indegree = [0]*(n+1)
    table = {}
    for i in range(1,n+1):
        table[i] = [set(),set()]
    for result in results:
        win,lose = result
        indegree[win]+=1
        table[win][1].add(lose)
        table[lose][0].add(win)
    queue = deque([])
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
    table = update_ranking(table,deepcopy(indegree),deepcopy(queue))
    for node in table:
        if len(table[node][0]|table[node][1])==n-1:
            answer+=1
    return answer