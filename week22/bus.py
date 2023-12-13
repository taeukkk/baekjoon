from heapq import heappush,heappop
def get_int(time):
    h,m = time.split(":")
    return int(h)*60+int(m)
def get_str(time):
    str_time = ''
    h = time//60
    m = time%60
    if h<10:
        str_time += '0'+str(h)
    else:
        str_time += str(h)
    str_time += ":"
    if m<10:
        str_time += '0'+str(m)
    else:
        str_time += str(m)
    return str_time
def solution(n, t, m, timetable):
    answer = ''
    crew= []
    for time in timetable:
        heappush(crew,get_int(time))
    bus = {}
    bus_time = []
    for i in range(n):
        bt =  9*60+t*i
        bus[bt] = []
        bus_time.append(bt)
    i = 0
    while i<len(bus_time) and crew:
        idx = bus_time[i]
        if len(bus[idx])==m:
            i+=1
            continue
        c = heappop(crew)
        if idx>=c:
            bus[idx].append(c)
        else:
            heappush(crew,c)
            i+=1
    if len(bus[bus_time[-1]])==m:
        answer = get_str(bus[bus_time[-1]][-1]-1)
    else: # len(bus[bus_time[-1]]) < m
        answer = get_str(bus_time[-1])
    return answer