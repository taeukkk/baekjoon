def check(prev_num,next_num):# 바꾸어야하면 1
    lp = len(prev_num)
    ln = len(next_num)
    # if lp==4:
    #     return 0
    if ln==4:
        return 1
    if lp==1:
        if prev_num > next_num[1]:
            return 1
        else:
            return 0
    if ln==1:
        if prev_num[1] < next_num:
            return 1
        else:
            return 0
    if lp==ln and prev_num[1:] > next_num[1:]:
        return 1
    if lp < ln:
        if prev_num[1]>next_num[1]:
            return 1
        if prev_num[1] == next_num[1] and prev_num+next_num[0] >= next_num:
            return 1
    if lp > ln:
        if prev_num[1]<next_num[1]:
            return 1
        if prev_num[1] == next_num[1] and prev_num+next_num[0] <= next_num:
            return 1

    return 0

def solution(numbers):
    global order
    answer = ''
    table = {}
    nums = []

    for n in numbers:
        nums.append(str(n))
    nums.sort()

    for n in nums:
        if n[0] in table:
            table[n[0]].append(n)
        else:
            table[n[0]] = [n]
    for i in range(9,-1,-1):
        si = str(i)
        if si in table:
            t = table[si]
            for j in range(1,len(t)):
                for k in range(j,0,-1):
                    if check(t[k-1],t[k])==1:
                        t[k],t[k-1] = t[k-1],t[k]
                    else:
                        break
        # if index in table:
            # order = quicksort(table[index])
            for j in range(len(t)-1,-1,-1):
                answer+=t[j]

    return answer