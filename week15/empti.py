from itertools import product
def get_discount(hope):
    if hope<=10:
        return 0
    elif 10<hope<=20:
        return 1
    elif 20<hope<=30:
        return 2
    return 3

def get_price(discount,emoticons,hope):
    value = [0.9, 0.8, 0.7, 0.6]
    buy = get_discount(hope)
    max_idx = len(discount)
    price = 0
    for i in range(max_idx):
        if discount[i]>=buy:
            price+=value[discount[i]]*emoticons[i]
    return price

def check_sales(answer,sales):
    if answer[0]<sales[0]:
        return sales
    elif answer[0]==sales[0] and answer[1]<sales[1]:
        return sales
    return answer

def solution(users, emoticons):
    answer = [0,0]
    discount_case = list(product([0,1,2,3], repeat=len(emoticons)))
    for discount in discount_case:
        sales = [0,0]
        for user in users:
            price = get_price(discount,emoticons,user[0])
            if price>=user[1]:
                sales[0]+=1
            else:
                sales[1]+=price
        answer = check_sales(answer,sales)
    return answer