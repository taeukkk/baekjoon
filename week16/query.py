from bisect import bisect_left
from itertools import combinations

def get_score(score):
    if score =='-':
        return 0
    return int(score)

def get_key(conditions):
    result = ''
    for cond in conditions:
        if cond:
            result+=cond
    return result

def solution(info, query):
    answer = []
    info_map = {'':[]}
    for i in range(len(info)):
        splited_info = info[i].split(" ")
        score = int(splited_info[-1])
        info_map[''].append(score)
        for j in range(len(splited_info[:-1])):
            info_case = list(combinations(splited_info[:-1],j+1))
            for ic in info_case:
                key = ''.join(ic)
                if key in info_map:
                    info_map[key].append(score)
                else:
                    info_map[key] = [score]
    for key in info_map:
        info_map[key].sort()

    for q in query:
        cnt=0
        q = q.replace('and','').replace('-','')
        conditions = q.split(" ")
        score_cond = get_score(conditions[-1])
        key = get_key(conditions[:-1])
        if key in info_map:
            arr = info_map[key]
            cnt = len(arr)-bisect_left(arr,score_cond)
        answer.append(cnt)
    return answer