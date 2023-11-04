import math

def solution(fees, records):
    answer = []
    table = {}
    for r in records:
        row = r.split()
        time = [int(row[0][0:2]),int(row[0][3:5])]
        if row[1] in table:
            table[row[1]].append(time)
        else:
            table[row[1]] = [time]

    cars = list(table.keys())
    cars.sort()
    for c in cars:
        times = table[c]
        if len(times)%2 !=0:
            times.append([23,59])
        total_time = 0
        for i in range(0,len(times),+2):
            out_time = times[i+1][0]*60 + times[i+1][1]
            in_time = times[i][0]*60 + times[i][1]
            total_time += out_time-in_time
        answer.append(total_time)

    for i in range(len(answer)):
        free_time = answer[i]-fees[0]
        if free_time <= 0:
            answer[i] = fees[1]
        else:
            add_time = math.ceil(free_time/fees[2])
            answer[i] = fees[1]+add_time*fees[3]

    return answer