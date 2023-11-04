def solution(numbers):
    answer = [0]*len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and stack[-1][0]<numbers[i]:
            s = stack.pop()
            answer[s[1]] = numbers[i]
        stack.append([numbers[i],i])
    while stack:
        s = stack.pop()
        answer[s[1]] = -1
    return answer