def solution(order):    
    answer = []
    stack = []
    cnt = 0
    
    for i in range(1,len(order)+1):
        if i==order[cnt]:
            answer.append(order[cnt])
            cnt+=1
        else:
            stack.append(i)

        while stack and stack[-1]==order[cnt]:
            answer.append(stack.pop())
            cnt+=1
            
    return len(answer)