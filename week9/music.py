def split_code(musicinfo):
    info = []
    for i in range(len(musicinfo)-1):
        if musicinfo[i]=='#':
            continue
        if musicinfo[i+1]=='#':
            info.append("("+musicinfo[i:i+2]+")")
        else:
            info.append("("+musicinfo[i]+")")
    if musicinfo[i+1]!='#':
        info.append("("+musicinfo[i+1]+")")
    return info

def get_code(s,e,musicinfo):
    code = []
    info = split_code(musicinfo)
    order = 0
    while len(code)!=e-s:
        if order == len(info):
            order=0
        code.append(info[order])
        order+=1
    return "".join(code)

def solution(m, musicinfos):
    answer = ''
    result={}
    m = "".join(split_code(m))

    for info in musicinfos:
        music = info.split(',')
        start = int(music[0][0:2])*60+int(music[0][3:5])
        end = int(music[1][0:2])*60+int(music[1][3:5])
        code = get_code(start,end,music[3])
        if m in code:
            if end-start in result:
                result[end-start].append(music[2])
            else:
                result[end-start] = [music[2]]

    if not result:
        return '(None)'
    time = list(result.keys())
    time.sort(reverse=True)
    answer = result[time[0]][0]
    return answer