from collections import deque
def solution(enroll, referral, seller, amount):
    answer = []
    parent = {} # key:child, value:parent
    money = {}
    money['-'] = 0
    for i in range(len(enroll)):
        ref = referral[i]
        enr = enroll[i]
        money[enr] = 0
        parent[enr] = ref
    for i in range(len(seller)):
        s = seller[i]
        fee = int(amount[i]*10)
        profit = amount[i]*100-fee
        money[s] += profit
        queue = deque([s])
        while queue:
            q = queue.popleft()
            if q not in parent:
                continue
            p = parent[q]
            temp = fee
            fee = int(fee*0.1)
            profit = temp-fee 
            money[p] += profit
            if fee>0:
                queue.append(p)
    for e in enroll:
        answer.append(money[e])
    return answer