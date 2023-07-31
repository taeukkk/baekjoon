def fact(jump,big,small):
    f = 1
    for i in range(jump-big):
        f*=jump
        jump -=1
    for s in range(small):
        f= f//(s+1)
    return f

def solution(n):
    answer = 1
    two = int(n/2)
    one = n-two*2
    while two != 0:
        if two > one:
            answer += fact(one+two,two,one)
        else:
            answer += fact(one+two,one,two)
        two -=1
        one +=2
    
    return answer%1234567