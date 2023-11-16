from collections import deque
    
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    group = [set()]
    for cost in costs:
        island = set(cost[:2])
        if not group[0]:
            group[0] |= island
            answer+=cost[2]
            continue
        idx = []
        not_connect = 0
        for i in range(len(group)):
            if len(group[i]&island)==1:
                idx.append(i)
            elif len(group[i]&island)==2:
                not_connect = 1
        if not_connect==1:
            continue
        if not idx:
            group.append(island)
            answer+=cost[2]
        else:
            base = group[idx[0]]|set(cost[:2])
            answer+=cost[2]
            merged_group = []
            for i in range(len(group)):
                if i in idx:
                    base |= group[i]
                else:
                    merged_group.append(group[i])
            merged_group.append(base)
            group = merged_group
    return answer