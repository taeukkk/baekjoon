def check_bits(num):
    result = ''
    end = len(num)-1
    if num[end]=='0':
        return int(num,2)+1
    for i in range(end-1,-1,-1):
        if num[i]=='0' and i!=0:
            result = num[:i]+"10"+num[i+2:]
            break;
        if i==0:
            result = num[:2]+"10"+num[3:]

    return int(result,2)

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(check_bits(bin(n)))

    return answer