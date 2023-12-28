from copy import deepcopy

def check_answer(key_set,blank_set,N):
    if len(blank_set-key_set)!=0:
        return False
    for r,c in (key_set-blank_set):
        if 0<=r<N and 0<=c<N:
            return False
    return True

def solution(key, lock):
    M,N = len(key),len(lock)
    lock_blank = []
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 0:
                lock_blank.append((r,c))
    if not lock_blank: #lock == null
        return True
    key_case = {0:[],1:[],2:[],3:[]}
    for i in range(4):
        key_hom = []
        for r in range(M):
            for c in range(M):
                if key[r][c] == 1:
                    key_hom.append((r,c))
        if not key_hom: #key == null
            return False
        key_case[i] = key_hom
        prev_key = deepcopy(key)
        for r in range(M):
            for c in range(M):
                key[c][M-1-r] = prev_key[r][c]
    blank_set = set(lock_blank)
    for lb in lock_blank:
        for kc in key_case.values():
            for base in kc:
                key_set = set()
                for k in kc:
                    row = lb[0]+k[0]-base[0]
                    col = lb[1]+k[1]-base[1]
                    key_set.add((row,col))
                answer = check_answer(key_set,blank_set,N)
                if answer == True:
                    return answer
    return False