from collections import deque
def solution(picks, minerals):
    answer = 0
    tired = [{"diamond":1,"iron":1,"stone":1},{"diamond":5,"iron":1,"stone":1},{"diamond":25,"iron":5,"stone":1}]
    i = 0
    sub_minerals = []
    while i<sum(picks)*5:
        sub = minerals[i:i+5]
        result = []
        for j in range(3):
            temp = 0
            tir = tired[j]
            for s in sub:
                temp+=tir[s]
            result.append(temp)
        sub_minerals.append(result)
        i+=5
    sub_minerals.sort(key=lambda x:(-x[2],-x[1],-x[0]))
    sm = deque(sub_minerals) 
    for i in range(3):
        if picks[i]==0:
            continue
        for _ in range(picks[i]):
            if sm:
                mineral = sm.popleft()
                answer += mineral[i]
            else:
                break
    return answer