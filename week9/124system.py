div,rem = 0,0

def add(num):
    global div,rem
    if num==0:
        div-=1
        return '4'
    elif num==1:
        return '1'
    else:
        return '2'   
            
def solution(n):
    global div,rem
    div,rem = n//3, n%3
    answer = ''
    while div!=0:
        answer = add(rem)+answer
        rem = div%3
        div //= 3
    if div+rem!=0:
        answer = add(rem)+answer
    return answer