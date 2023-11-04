def solution(k, tangerine):
    answer = 0
    tan = set(tangerine)
    num = {}
    temp = []
    for i in tangerine:
        if i in num:
            num[i] +=1
        else:
            num[i] = 1
        # num.append(tangerine.count(i))
    for i in tan:
        temp.append(num[i])
    temp = sorted(temp,reverse=True)
    for i in temp:
        if i >= k:
            answer+=1
            k=0
            break
        else:
            answer+=1
            k-=i
    return answer