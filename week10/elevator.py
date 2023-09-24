def solution(storey):
    answer = 0
    while storey!=0:
        cnt=storey%10
        if cnt==0:
            storey = storey//10
        elif cnt>5:
            storey += (10-cnt)
            answer += (10-cnt)
        else:
            if cnt==5 and storey%100-storey%10>=50:
                storey += (10-cnt)
                answer += (10-cnt)
                continue
            answer += cnt
            storey-=cnt
    return answer