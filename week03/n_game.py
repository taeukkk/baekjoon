def change_num(num,n):
    table = {k:v for (k,v) in zip([i for i in range(10,16)],['A','B','C','D','E','F'])}
    result = []
    while num!=0:
        temp = int(num%n)
        if temp in table:
            result.append(table[temp])
        else:
            result.append(temp)
        num = int(num//n)
    result.reverse()
    return ''.join(str(r) for r in result)

def solution(n, t, m, p):
    answer = ''
    word = "0"
    start = 1
    while len(word)<=t*m:
        word += change_num(start,n)
        start+=1
    
    for i in range(p-1,t*m,m):
        answer += word[i]
    return answer