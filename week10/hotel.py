def get_minutes(time):
    t = time.split(":")
    return int(t[0])*60+int(t[1])

def solution(book_time):
    rooms,times = [],[]
    for bt in book_time:
        times.append([get_minutes(bt[0]),get_minutes(bt[1])])
    times.sort()

    for time in times:
        if not rooms:
            rooms.append([time])
        else:
            cnt = 0
            for room in rooms:
                if room[-1][0]<= time[0] < room[-1][1]+10:
                    cnt+=1
                else:
                    room.append(time)
                    break
            if cnt == len(rooms):
                rooms.append([time])
    return len(rooms)