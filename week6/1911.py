import math
n,l = map(int,input().split())
water = [list(map(int, input().split())) for _ in range(n)]
water.sort(key = lambda w: w[0])
result = []
answer = 0

while water:
    w = water.pop(0)
    wl = w[1]-w[0]
    bl = math.ceil(wl/l)
    if not result:
        result.append([w[0],w[0]+l*bl])
        answer += bl
    else:
        r = result[-1]
        if w[0]<r[1]<=w[1]:
            bl = math.ceil((w[1]-r[1])/l)
            result.append([r[1],r[1]+l*bl])
            answer += bl
        elif w[0] >= r[1]:
            result.append([w[0],w[0]+l*bl])
            answer += bl
            
print(answer)