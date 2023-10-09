from collections import deque
import heapq
def solution(n, k, enemy):
    if k>=len(enemy):
        return len(enemy)
    dead = 0
    answer = k
    shield = []
    enemy = deque(enemy)
    heapq.heapify(shield)
    for _ in range(k):
        heapq.heappush(shield,enemy.popleft())
    while dead<n and enemy:
        dead+=heapq.heappushpop(shield,enemy.popleft())
        answer+=1
    if dead>n:
        answer-=1
    return answer