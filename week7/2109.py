import heapq
import sys
input = sys.stdin.readline
N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
table.sort(key = lambda x :x[1])

answer = []
for t in table:
    heapq.heappush(answer,t[0])
    if len(answer)>t[1]:
        heapq.heappop(answer)

print(sum(answer))
