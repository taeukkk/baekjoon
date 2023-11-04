from collections import deque

def solution(record):
    answer,uids = [],[]
    inout,name = {},{}

    for rec in record:
        r = rec.split()
        uids.append(r[1])
        if r[0] == "Leave":
            inout[r[1]].append("님이 나갔습니다.")
        elif r[0] == "Enter":
            name[r[1]] = r[2]
            if r[1] in inout:
                inout[r[1]].append("님이 들어왔습니다.")
            else:
                inout[r[1]] = deque(["님이 들어왔습니다."])
        else:
            name[r[1]] = r[2]
            uids.pop()

    for uid in uids:
        message = inout[uid].popleft()
        answer.append(name[uid]+message)
        
    return answer