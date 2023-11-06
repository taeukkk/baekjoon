def solution(cap, n, deliveries, pickups):
    answer = 0
    d_sum,p_sum = 0,0
    for i in range(n-1,-1,-1):
        d_sum -= deliveries[i]
        p_sum -= pickups[i]
        move = 0
        while d_sum<0 or p_sum<0:
            d_sum+=cap
            p_sum+=cap
            move+=1
        answer += (i+1)*2*move
    return answer