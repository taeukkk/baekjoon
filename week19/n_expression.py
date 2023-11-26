from itertools import product

def update_exp(exp,key,values):
    for val in values:
        if val==0:
            continue
        if key in exp:
            exp[key].add(val)
        else:
            exp[key] = set([val])
    return exp

def solution(N, number):
    answer = -1
    exp = {}
    if N==1:
        exp[1] = set([1])
    else:
        exp[2] = set([1])
    for i in range(1,9):
        val = int(str(N)*i)
        exp = update_exp(exp,i,[val])
    for i in range(1,9):
        for j in range(i,9-i):
            values = list(product(exp[i],exp[j]))
            for v in values:
                max_v = max(v[0],v[1])
                min_v = min(v[0],v[1])
                v_case = [v[0]+v[1],v[0]*v[1],max_v-min_v,max_v//min_v]
                exp = update_exp(exp,i+j,v_case)
    for k in sorted(list(exp.keys())):
        if number in exp[k]:
            return k
    return answer