from itertools import permutations
bingo = [set(['0/0','0/1','0/2']),set(['1/0','1/1','1/2']),set(['2/0','2/1','2/2']),
        set(['0/0','1/0','2/0']),set(['0/1','1/1','2/1']),set(['0/2','1/2','2/2']),
        set(['0/0','1/1','2/2']),set(['0/2','1/1','2/0'])]

def get_sub(idxs,mark): #두 자리씩 자르기
    if len(idxs)==2:
        return mark[idxs[0]] + mark[idxs[1]]
    return mark[idxs[0]]

def check_order(sub): #순서 파악 가능
    if len(sub)==2 and sub!='OX':
        return 0
    if len(sub)==1 and sub=='X':
        return 0
    return 1 #no problem

def check_bingo(idxs):
    for bg in bingo:
        if bg & idxs == bg:
            return 1
    return 0

def solution(board):
    idx = []
    mark = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]!='.':
                temp = str(i)+"/"+str(j)
                idx.append(temp)
                mark[temp] = board[i][j]

    orders = list(permutations(idx,len(idx)))
    for order in orders:
        mistake = 0
        sub = ''
        o_idx = set()
        x_idx = set()
        for i in range(0,len(order),2):
            temp = order[i:i+2]
            sub = get_sub(temp,mark)
            if check_order(sub) == 0:
                mistake = 1
                break
        if mistake == 0: 
            for i in range(len(order)):
                if mark[order[i]]=='O':
                    o_idx.add(order[i])
                else:
                    x_idx.add(order[i])
            o_bingo = check_bingo(o_idx)
            x_bingo = check_bingo(x_idx)
            if o_bingo==1 and x_bingo==1:
                continue
            elif o_bingo==1 and mark[order[-1]]=='O':
                return 1
            elif x_bingo==1 and mark[order[-1]]=='X': 
                return 1
            elif o_bingo==0 and x_bingo==0:
                return 1
    return 0