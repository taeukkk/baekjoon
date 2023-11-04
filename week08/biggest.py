def solution(numbers):
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
                    if t[k-1]+t[k] > t[k]+t[k-1]:
                        t[k],t[k-1] = t[k-1],t[k]
                    else:
                        break
            for j in range(len(t)-1,-1,-1):
                answer+=t[j]
                
    if set(answer) == {'0'}:
        answer = '0'
    return answer