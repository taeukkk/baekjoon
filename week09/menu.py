import itertools
result = {}
def add_result(menu):
    for i in range(len(menu),1,-1):
        sub_menu = list(itertools.combinations(menu,i))
        for j in range(len(sub_menu)):
            m = "".join(sorted(sub_menu[j]))
            if m in result:
                result[m] +=1
            else:
                result[m] =1

def solution(orders, course):
    answer = []
    cnt = {}
    for c in course:
        cnt[c] = 2
    for i in range(len(orders)):
        add_result(set(orders[i]))
    reverse_res = list(result.items())
    reverse_res.sort(key=lambda x: x[1],reverse=True)
    for r in reverse_res:
        lr = len(r[0])
        if lr in course and cnt[lr] <= r[1]:
            cnt[lr]=r[1]
            answer.append(r[0])
    answer.sort()
    return answer
