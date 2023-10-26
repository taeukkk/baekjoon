answer = []
def up_down(alpha):
    left = abs(ord('A')-ord(alpha))
    right = 26-left
    return min(left,right)

def left_right(name_alpha,visited,prev,direction,cnt):
    visited[prev]=1
    if sum(visited)==len(name_alpha):
        answer.append(cnt)
        return
    idx,move=0,1
    if direction==1:
        idx = (prev+1)%len(name_alpha)
        while idx!=prev:
            if visited[idx]==0:
                break
            idx = (idx+1)%len(name_alpha)
            move+=1
        cnt += move
    else: #direction == -1
        idx = minus_idx(prev,len(name_alpha)-1)
        while idx!=prev:
            if visited[idx]==0:
                break
            idx = minus_idx(idx,len(name_alpha)-1)
            move+=1
        cnt += move
    left_right(name_alpha,visited[:idx]+[1]+visited[idx+1:],idx,1,cnt)
    left_right(name_alpha,visited[:idx]+[1]+visited[idx+1:],idx,-1,cnt)

def minus_idx(idx,max_idx):
    if idx-1<0:
        return max_idx
    return idx-1 

def solution(name):
    global answer
    base = 0
    name_alpha = []
    visited = [0]*len(name)
    for i in range(len(name)):
        alpha = name[i]
        name_alpha.append(alpha)
        if alpha=='A':
            visited[i] = 1
        else:
            base+=up_down(alpha) 
    left_right(name_alpha,visited,0,1,0)
    left_right(name_alpha,visited,0,-1,0)
    return base+min(answer)