def solution(bridge_length, weight, truck_weights):
    bridge = []
    time = []
    tik = 0

    while truck_weights:
        tik+=1
        if time and tik-time[0]==bridge_length:
            bridge.pop(0)
            time.pop(0)
        if sum(bridge)+truck_weights[0]<=weight:
            bridge.append(truck_weights.pop(0))
            time.append(tik)
    
    return tik+bridge_length