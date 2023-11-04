def solution(land):
    r = len(land)
    c = len(land[0])
    table = [[0]*c for _ in range(r)]
    table = [land[0]]
    for i in range(1,r):
        route = []
        for j in range(c):
            route.append(max([land[i][j] + table[i-1][k] for k in range(c) if j!=k]))
        table.append(route)
        
    return max(table[r-1])