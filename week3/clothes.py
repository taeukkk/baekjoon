import itertools
def solution(clothes):
    table = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] in table:
            table[cloth[1]].append(cloth[0])
        else:
            table[cloth[1]] = [cloth[0]]
    table = list(table.values())   
    size = []
    for t in table:
        answer *= (len(t)+1)
    
    return answer-1