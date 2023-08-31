import sys
input = sys.stdin.readline
n,k = map(int,input().split())
order = list(map(int,input().split()))
answer = 0
plug = set()
table = {}
for i in range(k):
    if order[i] in table:
        table[order[i]].append(i)
    else:
        table[order[i]] = [i]

def check_plug():
    last_order = [-1,-1]
    for p in plug:
        if len(table[p])==0:
            return p
        elif table[p][0]>last_order[0]:
            last_order = [table[p][0],p]
    return last_order[1]
    
for elec in order:
    if len(plug)<n:
        plug.add(elec)
        table[elec].pop(0)
    elif elec not in plug:
        plug.remove(check_plug())
        plug.add(elec)
        table[elec].pop(0)
        answer +=1
    else:
        table[elec].pop(0)

print(answer)