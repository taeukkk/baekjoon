from itertools import combinations,product
def solution(user_id, banned_id):
    answer = 0
    ban_case,matched_id = {},{}
    for bi in banned_id:
        if bi in ban_case:
            ban_case[bi]+=1
        else:
            ban_case[bi]=1
        if bi not in matched_id:
            matched_id[bi] = []
    for bi in list(matched_id.keys()):
        for ui in user_id:
            if len(bi)!=len(ui):
                continue
            else: #len(bi)==len(ui)
                cnt = 0
                for i in range(len(bi)):
                    if bi[i]=='*' or bi[i]==ui[i]:
                        cnt+=1
                if cnt == len(bi):
                    matched_id[bi].append(ui)
    comb = []
    for key in list(matched_id.keys()):
        comb.append(list(combinations(matched_id[key],ban_case[key])))
    prod = list(product(*comb))
    result = []
    for p in prod:
        total_set = set()
        for user in p:
            total_set |= set(user)
        if len(total_set)==len(banned_id) and total_set not in result:
            answer+=1
            result.append(total_set)
    return answer