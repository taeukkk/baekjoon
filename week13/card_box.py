import itertools
def search_cards(start,cards,opened):
    i = start
    result = []
    while opened[i]==0:
        opened[i]=1
        result.append(i+1)
        i = cards[i]-1
    return result
def solution(cards):
    answer = 0
    result = []
    opened = [0]*len(cards)
    for i in range(len(cards)):
        if opened[i]==0:
            result.append(search_cards(i,cards,opened))
    groups = list(itertools.combinations(result,2))
    for group in groups:
        answer = max(answer,len(group[0])*len(group[1]))
    return answer