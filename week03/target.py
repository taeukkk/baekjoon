from itertools import combinations
def get_sum(comb,num,target):
    nums = []
    for c in comb:
        temp = num - 2*sum(c)
        if temp == target:    
            nums.append(temp)
    return nums

def solution(numbers, target):
    answer = 0
    result = []
    num = sum(numbers)
    for i in range(1,len(numbers)+1):
        nCr = list(combinations(numbers,i))
        result.append(get_sum(nCr,num,target))
    for r in result:
        answer += len(r)
    return answer