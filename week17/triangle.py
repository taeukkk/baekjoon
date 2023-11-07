def solution(triangle):
    answer = 0
    h = len(triangle)
    answer = [[0]*(i+1) for i in range(h)]
    answer[0][0] = triangle[0][0]
    for i in range(h-1):
        for j in range(i+1):
            left = answer[i][j]+triangle[i+1][j]
            answer[i+1][j] = max(answer[i+1][j],left)
            right = answer[i][j]+triangle[i+1][j+1]
            answer[i+1][j+1] = max(answer[i+1][j+1],right)
    return max(answer[-1])