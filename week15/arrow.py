from itertools import combinations_with_replacement
def get_score(apeach,lion):
    score=[0,0]
    for i in range(11):
        if apeach[i]==0 and lion[i]==0:
            continue
        if apeach[i]>=lion[i]:
            score[0]+=10-i
        elif apeach[i]<lion[i]:
            score[1]+=10-i
    return score

def get_final(answer):
    str_list = []
    for i in range(len(answer)):
        tmp = ''
        for j in range(len(answer[i])-1,-1,-1):
            tmp+=str(answer[i][j])
        str_list.append([i,tmp])
    str_list.sort(key=lambda x:x[1])
    return answer[str_list[-1][0]]

def solution(n, info):
    result = []
    target = [x for x in range(11)]
    combination_case = list(combinations_with_replacement(target,n))
    lion_case = []
    for comb in combination_case:
        lion = [0]*11
        for i in comb:
            lion[i]+=1
        lion_case.append(lion)
    for lion in lion_case:
        score = get_score(info,lion)
        if score[0] < score[1]:
            result.append([score[1]-score[0],lion])
    if not result:
        return [-1]
    else:
        result.sort(key=lambda x:(-x[0],x[1]))
        answer =[]
        max_gap = result[0][0]
        for max_case in result:
            if max_case[0]==max_gap:
                answer.append(max_case[1])
            else:
                break
        return get_final(answer)