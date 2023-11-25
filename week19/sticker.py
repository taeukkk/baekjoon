def solution(sticker):
    L = len(sticker)
    if L==1:
        return sticker[0]
    no_end = [0]*L
    no_end[0]=sticker[0]
    no_end[1]=sticker[0]
    no_start = [0]*L
    no_start[1]=sticker[1]
    for i in range(2,L-1):
        no_end[i] = max(no_end[i-2]+sticker[i],no_end[i-1])
    for i in range(2,L):
        no_start[i] = max(no_start[i-2]+sticker[i],no_start[i-1])
    return max(no_end[-2],no_start[-1])