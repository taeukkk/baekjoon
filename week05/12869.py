from itertools import permutations
n = int(input())
scv = list(map(int,input().split()))
def solution():
    if n==1:
        return scv[0]//9 if scv[0]%9==0 else scv[0]//9+1
    elif n==2:
        scv.append(0)
    power = [9,3,1]
    attack = list(permutations(power,3))
    table = [[[0]*(scv[2]+1) for _ in range(scv[1]+1)] for _ in range(scv[0]+1)]
    for x in range(scv[0],-1,-1):
        for y in range(scv[1],-1,-1):
            for z in range(scv[2],-1,-1):
                s = [x,y,z]
                if s != scv and table[x][y][z]==0:
                    continue
                for a in attack:
                    s = [x,y,z]
                    for i in range(3):
                        temp = s[i]-a[i]
                        if temp<0:
                            s[i]=0
                        else:
                            s[i]=temp
                    if table[s[0]][s[1]][s[2]]==0 or table[s[0]][s[1]][s[2]]>table[x][y][z]+1:
                        table[s[0]][s[1]][s[2]] = table[x][y][z]+1
    return table[0][0][0]

print(solution())