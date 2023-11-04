from collections import deque
def solution(elements):
    result = set([])
    queue = deque()
    size = len(elements)
    for i in range(1,size+1):
        queue = deque()
        for k in range(0,i):
            queue.append(elements[k])
        result.add(sum(queue))
        for j in range(i,i+size):
            queue.popleft()
            queue.append(elements[j%size])
            result.add(sum(queue))

    return len(result)