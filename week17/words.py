answer = 51
def dfs(now, target, words, visited, result):
    global answer
    if now==target:
        answer = min(answer,result)
        return
    next_words = []
    for i in range(len(words)):
        cnt = 0
        if visited[i]==0:
            for j in range(len(words[i])):
                if now[j]!=words[i][j]:
                    cnt+=1
            if cnt==1:
                next_words.append([i,words[i]])
    for word in next_words:
        dfs(word[1], target, words, visited[:word[0]]+[1]+visited[word[0]+1:], result+1)

def solution(begin, target, words):
    global answer
    visited = [0]*len(words)
    next_words = []
    for i in range(len(words)):
        cnt = 0
        for j in range(len(words[i])):
            if begin[j]!=words[i][j]:
                cnt+=1
        if cnt==1:
            next_words.append([i,words[i]])
    for now in next_words:
        dfs(now[1], target, words, visited[:now[0]]+[1]+visited[now[0]+1:], 1)
    if answer ==51:
        return 0
    return answer