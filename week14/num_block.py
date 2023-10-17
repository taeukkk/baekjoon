import math
def get_num(block):
    result = 0
    for i in range(2,int(math.sqrt(block))+1):
        if i==block:
            continue
        if block%i==0:
            result = block//i
            if result > 10**7:
                continue
            return result
    if result!=0:
        return block//result
    return 1

def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(get_num(i))
    if begin==1:
        answer[0]=0
    return answer