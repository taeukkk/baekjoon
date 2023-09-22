import math
def count(number):
    result = 1
    for num in range(1,number+1):
        result*=num
    return result
    
def solution(n, k):
    answer = []
    num = [i for i in range(1,n+1)]
    while len(num)!=1:
        width = count(len(num))//n
        index = math.ceil(k/width)-1
        answer.append(num[index])
        del num[index]
        n-=1
        k-=width*index
    answer.append(num.pop())
    return answer