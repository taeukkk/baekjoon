n = int(input())
result = 0
stack = []

for _ in range(n):
    hei = int(input())
    while stack and stack[-1][0] < hei:
        result+=stack.pop()[1]

    if len(stack) < 1 :
        # print("case: null")
        stack.append([hei,1])
    
    elif stack[-1][0] > hei:
        # print("case: A>B")
        result+=1
        stack.append([hei,1])

    elif stack[-1][0] ==hei:
        # print("case A=B")
        result+=stack[-1][1]
        stack[-1][1] +=1

        if len(stack)>1:
            result+=1
        # result+=stack[-1][1]       
    # print(stack,"/",result)
            
print(result)
    