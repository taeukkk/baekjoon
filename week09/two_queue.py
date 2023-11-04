from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    l = len(queue1)

    if (sum1+sum2)%2 != 0:
        return -1
    while answer<=3*l:
        if sum1==sum2:
            return answer;
        elif sum1>sum2:
            one = queue1.popleft()
            sum1-=one
            sum2+=one
            queue2.append(one)
            answer +=1
        else:
            two = queue2.popleft()
            sum2-=two
            sum1+=two
            queue1.append(two)
            answer+=1
    return -1