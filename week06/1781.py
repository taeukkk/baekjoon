import heapq
n = int(input())
table = []
for _ in range(n):
    deadline, cup = map(int,input().split())
    heapq.heappush(table,(deadline,-cup))
select = []
answer = 0

while table:
    p = heapq.heappop(table)
    if p[0]>len(select):
        heapq.heappush(select,(-p[1],p[0]))
        answer -= p[1]
    elif select[0][0] < -p[1]:
        out = heapq.heapreplace(select, (-p[1],p[0]))
        answer -= out[0]
        answer -= p[1]
        
print(answer)