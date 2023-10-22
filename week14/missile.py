from collections import deque
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    queue = deque(targets)
    attack_point = queue.popleft()[1]-0.5
    while queue:
        q = queue.popleft()
        if q[0]>attack_point:
            answer+=1
            attack_point = q[1]-0.5
    return answer+1