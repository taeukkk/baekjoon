def solution(prices):
    answer = [0]*len(prices)
    stack = [[prices[0],0]]
    for i in range(1,len(prices)):
        while stack and stack[-1][0] >prices[i]:
            temp = stack.pop()
            answer[temp[1]] = i-temp[1]
        stack.append([prices[i],i])
    while stack:
        temp = stack.pop()
        answer[temp[1]] = i-temp[1]
    return answer