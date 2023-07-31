def solution(s):
    table = {')':'(',']':'[','}':'{'}
    size = len(s)
    answer = 0
    for i in range(size):
        stack = []
        for j in range(i,i+size):
            temp = s[j%size]
            if not stack or temp == '(' or temp == '[' or temp =='{':
                stack.append(temp)
            elif stack[-1] == table[temp]:
                stack.pop()
        if len(stack)==0:
            answer +=1
    return answer