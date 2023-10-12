from itertools import combinations
def array_to_str(array):
    result = ''
    for a in array:
        result+=str(a)+'/'
    return result[:-1]

def is_unique(key,relation):
    key = key.split('/')
    table = {}
    for row in relation:
        temp = []
        for i in range(len(key)):
            temp.append(row[int(key[i])])
        select = array_to_str(temp)
        if select in table:
            return 0
        else:
            table[select] = 1
    return 1

def in_another(set1,set2):
    joint = set1 & set2
    if joint==set1 or joint==set2:
        return 1
    return 0

def solution(relation):
    answer = []
    for i in range(len(relation[0])):
        if is_unique(str(i),relation)==1:
            answer.append(set([i]))
    num=2
    while num<=len(relation[0]):
        candidates = list(combinations([x for x in range(len(relation[0]))],num))
        for candi in candidates:
            skip = 0
            set_candi = set(candi)
            str_candi = array_to_str(candi)
            for key in answer:
                if in_another(set_candi,key)==1:
                    skip = 1
                    break
            if skip == 1:
                continue
            if is_unique(str_candi,relation)==1:
                answer.append(set_candi)
        num+=1
    return len(answer)