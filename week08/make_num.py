def solution(x, y, n):
    answer = 1000001
    queue = [[y,0]]
    while queue:
        q = queue.pop(0)
        if x>q[0]:
            continue;
        if q[0]==x and q[1]<answer:
            answer = q[1]
            continue;
        if q[0]%2==0:
            queue.append([q[0]/2,q[1]+1])
        if q[0]%3==0:
            queue.append([q[0]/3,q[1]+1])
        queue.append([q[0]-n,q[1]+1])
    
    if answer == 1000001:
        return -1
    return answer