import math
def solution(r1, r2):
    answer = 0
    axis = r2-r1+1
    for x in range(1,r2):
        y2_2 = math.pow(r2,2)-math.pow(x,2)  
        y2 = math.floor(math.sqrt(y2_2))
        y1 = 1
        if x<r1:
            y1_2 = math.pow(r1,2)-math.pow(x,2)
            y1 = math.ceil(math.sqrt(y1_2))
        answer+=y2-y1+1
    answer *= 4 
    answer += 4*axis 
    return answer