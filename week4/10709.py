h,w = map(int, input().split())
sky = [input() for _ in range(h)]
result = []

for row in sky:
    stack = []
    for col in row:
        if col == 'c':
            stack.append(0)
        elif stack and stack[-1] >=0:
            stack.append(stack[-1]+1)
        else:
            stack.append(-1)
    result.append(" ".join(str(s) for s in stack))
    
for row in result:
    print(row)