def add_dict(dic,gen,data):
    if gen in dic:
        dic[gen] += data
    else:
        dic[gen] = data
            
def solution(genres, plays):
    answer = []
    melon = {}
    cnt = {}
    for i in range(len(genres)):
        add_dict(melon,genres[i],[[plays[i],i]])
        add_dict(cnt,genres[i],plays[i])
    order = sorted(cnt.items(),key = lambda x:-x[1])
    for gen in order:
        music = melon[gen[0]]
        music.sort(key=lambda x:(-x[0],x[1]))
        if len(music)>1:
            top = [music[0][1],music[1][1]]
            answer+=top
        else:
            answer.append(music[0][1])
    return answer