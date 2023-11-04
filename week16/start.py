from itertools import combinations

def get_point(lines):
    A = lines[0][0]
    B = lines[0][1]
    E = lines[0][2]
    C = lines[1][0]
    D = lines[1][1]
    F = lines[1][2]
    if A*D==B*C:
        return None
    else:
        return [(B*F-E*D)/(A*D-B*C),(E*C-A*F)/(A*D-B*C)]
   
def solution(line):
    answer = []
    x,y = [],[]
    select_line = list(combinations(line,2))
    for sl in select_line:
        p = get_point(sl)
        if p ==None:
            continue
        if p[0]==int(p[0]) and p[1]==int(p[1]):
            x.append(int(p[0]))
            y.append(int(p[1]))

    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)
    dx = max_x-min_x
    dy = max_y-min_y

    result = [['.']*(dx+1) for _ in range(dy+1)]
    for i in range(len(x)):
        col = x[i]-min_x
        row = -(y[i]-max_y)
        result[row][col] = '*'
    for line in result:
        answer.append(''.join(line))
    return answer