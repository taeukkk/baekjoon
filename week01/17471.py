import copy
import itertools

def get_group(index,temp,path):
    if index in path:
        temp.append(index)
        path.remove(index)
        for j in range(1,len(table[index])):
            if table[index][j] in path:
                get_group(table[index][j],temp,path)
    return temp

def divide_two(group_one):
    group_two = [i for i in range(1,n+1) if i not in group_one]
    visit = copy.deepcopy(group_two)
    num_group = []
    while len(visit)!=0:
        for v in visit:
            num_group.append(get_group(v,[],visit))

    if len(num_group)==1:
        gap = sum([table[0][i-1] for i in group_one])
        return abs(result-2*gap)
    return -1
    
n = int(input())
table = [list(map(int, input().split())) for _ in range(n+1)]
visit = [v for v in range(1,n+1)]
group = []
result = sum(table[0])

# 1. 그룹 확인 (v)
# 2. 2개이하 or 초과
# 3. 인구수 파악 -> 가장 많은 지점 우선

while len(visit)!=0:
    for v in visit:
        group.append(get_group(v,[],visit))

if len(group) >2:
    print(-1)
else:
    if len(group) == 2:
        gap = 0
        for i in group[0]:
            gap += table[0][i-1]
        print(abs(result-2*gap))
    else: # one group
        results = []
        for num in range(1,int(n/2)+1):
            div_group = list(itertools.combinations([i for i in range(1,n+1)], num))
            for d in div_group:
                path = [i for i in d]
                num_group = []
                while len(path)!=0:
                    for p in path:
                        num_group.append(get_group(p,[],path))
                if len(num_group)==1:
                    gap = divide_two(d)
                    if gap!=-1:
                        results.append(gap)
        print(min(results))
