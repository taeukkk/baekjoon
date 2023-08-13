from itertools import product

alpha = ['A','E','I','O','U']
def solution(word):
    result = []
    table = {}
    for i in range(1,6):
        pi = list(product(alpha,repeat = i))
        for p in pi:
            temp = ''
            for t in p:
                temp += t
            result.append(temp)
    result.sort()
    
    for i in range(len(result)):
        table[result[i]] = i+1

    return table[word]
