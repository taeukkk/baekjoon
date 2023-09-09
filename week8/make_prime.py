from itertools import permutations

def is_prime(num):
    if num<2:
        return 0
    for i in range(2,int(num**(1/2))+1):
        if num%i ==0:
            return 0
    return 1

def make_num(candi,len_num):
    result = set()
    max_num = 10**len_num
    min_num = 10**(len_num-1)
    for c in candi:
        num = ""
        for i in range(len(c)):
            num+=c[i]
        num = int(num)
        if min_num<=num<max_num:
            result.add(int(num))
    return result

def solution(numbers):
    answer = 0
    nums = []
    for n in numbers:
        if is_prime(int(n))==1 and n not in nums:
            answer+=1
        nums.append(n)

    for i in range(2,len(nums)+1):
        nPr = set(permutations(nums,i))
        for n in make_num(nPr,i):
            if is_prime(n)==1:
                answer+=1
    return answer