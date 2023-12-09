def get_answer(max_S,min_S):
    if max_S*min_S>0:
        return max(abs(max_S),abs(min_S))
    return abs(max_S-min_S)

def solution(sequence):
    answer = 0
    L = len(sequence)
    if L==1:
        return abs(sequence[0])
    S = [0]*L
    pulse = []
    for i in range(L):
        if i%2==0:
            pulse.append(sequence[i])
        else:
            pulse.append(-sequence[i])
    S[0] = pulse[0]
    for i in range(1,L):
        S[i] = S[i-1]+pulse[i]
    answer = get_answer(max(S),min(S))
    return answer