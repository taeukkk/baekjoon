from collections import deque
def solution(priorities, location):
    result = []
    queue = deque(priorities)
    num = deque([i for i in range(len(priorities))])
    me = [priorities[location],num[location]]
    
    while queue:
        temp = [queue.popleft(),num.popleft()]
        if queue and max(queue) > temp[0]:
            queue.append(temp[0])
            num.append(temp[1])
        else:
            result.append(temp[0])
            if temp[1] == me[1]:
                break
    
    return len(result)