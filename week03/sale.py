from collections import deque
import copy
def get_dict(list):
    result = {}
    for l in list:
        if l in result:
            result[l] +=1
        else:
            result[l]=1
    return result
def solution(want, number, discount):
    answer = 0
    items = dict(zip(want,number))
    days = sum(number)
    cart = deque()
    table = {}
    for d in discount:
        if len(cart)==days:
            table = get_dict(cart)
            if table == items:
                answer+=1
            cart.popleft()
            cart.append(d)
        else:
            if d in items:
                cart.append(d)
            else:
                cart.clear()
    if table == items:
        answer+=1
    return answer