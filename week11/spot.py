def f(x,b):
    return -x+b
def check_distance(x,y,R):
    if x**2+y**2<=R**2:
        return 1
    return 0

def solution(k,d):
    answer = 0
    R = d/k
    r = int(R)
    base = [0]*(r+1)
    base[0]=1
    for i in range(1,r+1):
        base[i] = base[i-1]+(i+1)
        
    y_ic = r+1
    max_x = r
    min_y = f(max_x,y_ic)
    while max_x>=min_y:
        if check_distance(min_y,max_x,R)==1:
            answer+=(max_x-min_y+1)
            y_ic+=1
        else:
            max_x-=1
        min_y = f(max_x,y_ic)
    return answer+base[r]