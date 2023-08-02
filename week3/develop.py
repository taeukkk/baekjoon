import math
def solution(progresses, speeds):    
    answer = []
    temp = 0
    days = 0
    for i in range(len(progresses)):
        progresses[i] += days*speeds[i]
        if progresses[i] <100:
            if temp!=0:
                answer.append(temp)
            temp=1
            days += math.ceil((100-progresses[i])/speeds[i])
        else:
            temp+=1
    answer.append(temp)
    return answer