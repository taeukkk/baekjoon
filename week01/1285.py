import copy
def check_coin(table):
    count = 0
    for r in table:
        for c in range(len(r)):
            if r[c] =='T':
                count +=1
    return count

def check_table(table):
    back = []
    for r in table:
        count = 0
        for c in range(len(r)):
            if r[c] =='T':
                count+=1
        back.append(count)
    for c in range(len(table)):
        count = 0
        for r in table:
            if r[c] =='T':
                count+=1
        back.append(count)
    return [i for i in range(len(back)) if back[i]==max(back)]


def flip(coin):
    if coin =='H':
        return 'T'
    return 'H'

def flip_table(copy_table,line,n):
    if line < n:
        for i in range(n):
            copy_table[line][i] = flip(copy_table[line][i])
    else:
        for i in range(n):
            copy_table[i][line%n] = flip(copy_table[i][line%n])
    return copy_table

n = int(input())
table = [list(input()) for _ in range(n)]
numT = check_coin(table)
candi = check_table(table)
table_list = [flip_table(copy.deepcopy(table),l,n) for l in candi]
count = [check_coin(t) for t in table_list]

while True:
    if min(count) >= numT:
        break;
    numT = min(count)
    candi = [check_table(t) for t in table_list]
	  # candi = [check_table(table_list[i]) for i in range(len(table_list)) if count[i] == numT]
    table_list = [flip_table(copy.deepcopy(t),c[i],n) for t in table_list for c in candi for i in range(len(c))]
    count = [check_coin(t) for t in table_list]
    
print(numT)