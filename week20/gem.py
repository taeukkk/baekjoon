from collections import Counter

def add_gem(dic,gem):
    if gem in dic:
        dic[gem]+=1
    else:
        dic[gem]=1

def del_gem(dic,gem):
    dic[gem]-=1
    if dic[gem]==0:
        dic.pop(gem)

def update_answer(gems,dic,start,end,answer):
    gap_now = end-start
    gap_answer = answer[1]-answer[0]
    if gap_now == gap_answer:
        if start < answer[0]:
            answer = [start,end]
    elif gap_now < gap_answer:
        answer = [start,end]
    del_gem(dic,gems[start])
    start+=1  
    return answer

def solution(gems):
    answer = [0,len(gems)]
    num_gem = len(Counter(gems).keys())
    start,end=0,0
    select = {}
    while end!=len(gems):
        if not select or len(select.keys())!=num_gem:
            add_gem(select,gems[end])
            end+=1
        else:
            answer = update_answer(gems,select,start,end-1,answer)
            start+=1
    while start<end:
        if len(select.keys())==num_gem:
            answer = update_answer(gems,select,start,end-1,answer)
            start+=1
        else:
            break
    return [answer[0]+1,answer[1]+1]