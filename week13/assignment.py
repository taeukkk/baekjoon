def get_time(time):
    info = time.split(":")
    return int(info[0])*60+int(info[1])

def solution(plans):
    answer = []
    stay = []  
    plans.sort(key = lambda x:get_time(x[1]))

    for i in range(len(plans)-1):
        gap = get_time(plans[i+1][1])-get_time(plans[i][1])
        if gap < int(plans[i][2]):
            stay.append(plans[i][0:2]+[int(plans[i][2])-gap])
        else: # gap >= int(plans[i][2])
            answer.append(plans[i][0])
            left = gap-int(plans[i][2])
            while left and stay:
                latest = stay.pop()
                if int(latest[2]) <= left:
                    answer.append(latest[0])
                    left-=int(latest[2])
                else:
                    stay.append(latest[0:2]+[int(latest[2])-left])
                    left=0
    answer.append(plans[-1][0])
    while stay:
        answer.append(stay.pop()[0])
    return answer