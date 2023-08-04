from itertools import permutations
def solution(k, dungeons):
    result = []
    route = list(permutations(dungeons,len(dungeons)))
    for r in route:
        temp = k
        move = 0
        for d in r:
            if temp>=d[0]:
                temp-=d[1]
                move+=1
            else:
                break
        if move!=0:
            result.append(move)
            
    return max(result)