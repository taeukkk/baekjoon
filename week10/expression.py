from itertools import permutations
def calculate(exp,op):
    result = int(exp[0])
    if op == '+':
        for i in range(1,len(exp)):
            result+=int(exp[i])
    elif op == '-':
        for i in range(1,len(exp)):
            result-=int(exp[i])
    else:
        for i in range(1,len(exp)):
            result*=int(exp[i])
    return result

def split_exp(exp,op,cnt):
    result=[]
    if cnt == len(op)-1:
        tmp = exp.split(op[cnt])
        return calculate(tmp,op[cnt])
    sub_exp = exp.split(op[cnt])
    for sub in sub_exp:
        if not sub.isnumeric():
            result.append(split_exp(sub,op,cnt+1))
        else:
            result.append(sub)
    return result

def solution(expression):
    answer = 0
    operation = []
    if "+" in expression:
        operation.append("+")
    if "-" in expression:
        operation.append("-")
    if "*" in expression:
        operation.append("*")
    if len(operation)>1:
        ops = list(permutations(operation,len(operation)))
    else:
        return abs(split_exp(expression,operation,0))

    for op in ops:
        splited = split_exp(expression,op,0)
        for i in range(len(splited)):
            if type(splited[i])==list:
                if len(splited[i])==1:
                    splited[i] = splited[i][0]
                else:
                    splited[i] = calculate(splited[i],op[1])
        result = splited[0]
        for i in range(1,len(splited)):
            result = calculate([result,splited[i]],op[0])
        answer = max(answer,abs(result))
    return answer