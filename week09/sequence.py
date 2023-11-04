sum_p,index_p = 0,0
portion,answer = [],[]
    
def plus(item,i):
    global sum_p
    portion.append(item)
    sum_p += item

def minus():
    global sum_p,index_p
    sum_p -= portion[index_p]
    index_p+=1
    
def check_answer(i):
    global answer
    if not answer or answer[1]-answer[0]+1>i-index_p:
        answer = [index_p,i-1]

def solution(sequence,k):
    i=0
    
    while i != len(sequence):
        if sum_p > k:
            minus()
        else:
            if sum_p == k:
                check_answer(i)
            plus(sequence[i],i)
            i+=1
    while portion:
        if sum_p < k:
            break
        if sum_p > k:
            minus()
        if sum_p == k:
            check_answer(i)
            minus()
            
    return answer