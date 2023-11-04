from collections import deque
tree ={}
visited = []

def make_tree(key,val):
    if key in tree:
        tree[key].append(val)
    else:
        tree[key] = [val]
def cut_tree(key,val):
    tree[key].remove(val)
    tree[val].remove(key)
def connect_tree(key,val):
    tree[key].append(val)
    tree[val].append(key)

def bfs(start):
    result = 0
    queue = deque([start])
    visited[start]=1
    while queue:
        q = queue.popleft()
        result+=1
        for t in tree[q]:
            if visited[t]==0:
                queue.append(t)
                visited[t]=1
    return result

def solution(n,wires):
    global tree,visited
    answer = 99
    for pair in wires:
        make_tree(pair[0],pair[1])
        make_tree(pair[1],pair[0])
    for w in wires:
        visited = [0]*(n+1)
        cut_tree(w[0],w[1])
        net1,net2 = 0,0
        for v in range(1,n+1):
            if visited[v]==0:
                if net1==0:
                    net1 = bfs(v)
                else:
                    net2 = bfs(v)
                    break;
        connect_tree(w[0],w[1])
        gap = abs(net1-net2)
        if gap<answer:
            answer = gap
    return answer