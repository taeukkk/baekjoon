def solution(data, col, row_begin, row_end):
    result = []
    data.sort(key = lambda x:(x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        S_i = 0
        for j in range(len(data[i-1])):
            S_i += data[i-1][j]%i
        result.append(S_i)
    answer = result[0]
    for i in range(1,len(result)):
        answer ^= result[i]
    return answer