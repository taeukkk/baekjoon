def solution(weights):
    answer = 0
    possible = [1, 1/2, 2, 2/3, 3/2, 3/4, 4/3]
    table = {}
    for w in weights:
        if w in table:
            table[w]+=1
        else:
            table[w]=1
    pairs = list(table.keys())
    for i in range(len(pairs)):
        cnt = 0
        for j in range(i+1,len(pairs)):
            if pairs[i]/pairs[j] in possible:
                cnt+=table[pairs[i]]*table[pairs[j]]
        val = table[pairs[i]]
        if val>1:
            cnt+=val*(val-1)//2
        answer+=cnt
    return answer