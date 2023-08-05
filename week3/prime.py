import math
def is_prime(num):
    if num =='':
        return 0
    num = int(num)
    if num==1:
        return 0
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i ==0:
            return 0
    return 1

def change_num(num,k):
    if k==10:
        return str(num)
    result = []
    i = 1
    while num!=0:
        up = k**i
        down = k**(i-1)
        result.append(int(num%up//down))
        num -= result[i-1]*down
        i+=1
    result.reverse()
    return ''.join(str(n) for n in result)

def solution(n, k):
    answer = 0
    num = change_num(n,k)
    zero = []
    for i in range(len(num)):
        if num[i]=='0':
            zero.append(i)
    print(zero)

    if len(zero)==0 :
        return is_prime(num)
    elif len(zero)==1:
        if zero[0] == 0:
            return is_prime(num[1:])
        elif zero[0] == len(num)-1:
            return is_prime(num[:len(num)-1])
        else:
            return is_prime(num[:zero[0]])+is_prime(num[zero[0]+1:])
    else:
        for i in range(len(zero)-1):    
            answer += is_prime(num[zero[i]+1:zero[i+1]])
        answer += is_prime(num[:zero[0]])
        answer += is_prime(num[zero[len(zero)-1]+1:])
    return answer