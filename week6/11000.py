import sys
import heapq
input = sys.stdin.readline
n = int(input())
time,room = [],[]
answer = 0

for _ in range(n):
    heapq.heappush(time,list(map(int,input().split())))
while time:
    t = heapq.heappop(time)
    if not room or room[0] > t[0]:
        heapq.heappush(room,t[1])
        answer+=1
    else:
        heapq.heapreplace(room,t[1])

print(answer)