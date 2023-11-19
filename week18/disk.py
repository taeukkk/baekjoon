def solution(jobs):
    answer = 0
    jobs.sort()
    table = {}
    for job in jobs:
        req,t = job
        if req in table:
            table[req].append([t,req])
        else:
            table[req] = [[t,req]]
    disk = []
    while True:
        if disk:
            disk.sort()
            select = disk.pop(0)
            end += select[0]
            answer += end-select[1]
        else:
            left = list(table.keys())
            if left:
                start = left[0]
                end = start+table[start].pop(0)[0]
                answer += end-start
                disk = table.pop(start)
            else:
                break
        left = list(table.keys())    
        for k in left:
            if k<=end:
                disk += table.pop(k)
            else:
                break
    return answer//len(jobs)