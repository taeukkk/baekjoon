import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
jewerly = [list(map(int,input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
jewerly.sort()
bag.sort()
answer = []
result = 0
cnt = 0

for j in jewerly:
    if cnt<K and j[0]<=bag[cnt]:
        heapq.heappush(answer,-j[1])
    else:
        while cnt<K and j[0]>bag[cnt]:
            if answer:
                result -= heapq.heappop(answer)
            cnt+=1
            if cnt<K and j[0]<=bag[cnt]:
                heapq.heappush(answer,-j[1])        
for _ in range(cnt,K):
    if answer:
        result -= heapq.heappop(answer)

print(result)